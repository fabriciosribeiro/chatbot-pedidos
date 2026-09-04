import gradio as gr
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "microsoft/DialoGPT-medium"
MAX_NEW_TOKENS = 50
MAX_HISTORY_TOKENS = 800


def carregar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model


tokenizer, model = carregar_modelo()


dados_pedidos = {
    "numero_pedido": ["12345", "67890", "11121", "22232"],
    "status": ["Shipped", "Processing", "Delivered", "Cancelled"],
}

df_status_pedidos = pd.DataFrame(dados_pedidos)


palavras_chave_status = [
    "order",
    "order status",
    "status of my order",
    "check my order",
    "track my order",
    "order update",
]


def verificar_status_pedido(numero_pedido):
    numero_pedido = str(numero_pedido).strip()

    resultado = df_status_pedidos[
        df_status_pedidos["numero_pedido"] == numero_pedido
    ]

    if not resultado.empty:
        status = resultado.iloc[0]["status"]
        return f"The status of your order {numero_pedido} is: {status}"

    return "Order number not found. Please check and try again."


def responder(input_usuario, ids_historico_chat):
    if any(
        keyword in input_usuario.lower()
        for keyword in palavras_chave_status
    ):
        return "Could you please enter your order number?", ids_historico_chat

    novo_usuario_input_ids = tokenizer.encode(
        input_usuario + tokenizer.eos_token,
        return_tensors="pt",
    )

    if ids_historico_chat is not None:
        bot_input_ids = torch.cat(
            [ids_historico_chat, novo_usuario_input_ids],
            dim=-1,
        )
    else:
        bot_input_ids = novo_usuario_input_ids

    bot_input_ids = bot_input_ids[:, -MAX_HISTORY_TOKENS:]

    with torch.no_grad():
        output_ids = model.generate(
            bot_input_ids,
            max_new_tokens=MAX_NEW_TOKENS,
            pad_token_id=tokenizer.eos_token_id,
        )

    resposta = tokenizer.decode(
        output_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True,
    ).strip()

    ids_historico_chat = output_ids[:, -MAX_HISTORY_TOKENS:]

    return resposta, ids_historico_chat


def processar_entrada(
    input_usuario,
    historico,
    ids_historico_chat,
    aguardando_numero_pedido,
):
    input_usuario = (input_usuario or "").strip()

    if not input_usuario:
        return (
            historico,
            ids_historico_chat,
            aguardando_numero_pedido,
            "",
        )

    if aguardando_numero_pedido:
        resposta = verificar_status_pedido(input_usuario)
        aguardando_numero_pedido = False
    else:
        resposta, ids_historico_chat = responder(
            input_usuario,
            ids_historico_chat,
        )

        if resposta == "Could you please enter your order number?":
            aguardando_numero_pedido = True

    historico = historico or []
    historico.append(
        {
            "role": "user",
            "content": input_usuario,
        }
    )
    historico.append(
        {
            "role": "assistant",
            "content": resposta,
        }
    )

    return (
        historico,
        ids_historico_chat,
        aguardando_numero_pedido,
        "",
    )


def limpar_conversa():
    return [], None, False, ""


with gr.Blocks(
    title="Sistema de Atendimento e Consulta de Pedidos",
) as app:
    gr.Markdown(
        """
        # Sistema de Atendimento e Consulta de Pedidos

        Interface para conversação e consulta do status de pedidos.
        """
    )

    chatbot = gr.Chatbot(
        label="Atendimento",
        height=500,
    )

    msg = gr.Textbox(
        placeholder="Digite sua mensagem...",
        label="Mensagem",
        lines=1,
    )

    with gr.Row():
        enviar = gr.Button("Enviar", variant="primary")
        limpar = gr.Button("Limpar conversa")

    estado = gr.State(None)
    aguardando_numero_pedido = gr.State(False)

    enviar.click(
        processar_entrada,
        inputs=[
            msg,
            chatbot,
            estado,
            aguardando_numero_pedido,
        ],
        outputs=[
            chatbot,
            estado,
            aguardando_numero_pedido,
            msg,
        ],
    )

    msg.submit(
        processar_entrada,
        inputs=[
            msg,
            chatbot,
            estado,
            aguardando_numero_pedido,
        ],
        outputs=[
            chatbot,
            estado,
            aguardando_numero_pedido,
            msg,
        ],
    )

    limpar.click(
        limpar_conversa,
        inputs=[],
        outputs=[
            chatbot,
            estado,
            aguardando_numero_pedido,
            msg,
        ],
    )


if __name__ == "__main__":
    app.launch()
