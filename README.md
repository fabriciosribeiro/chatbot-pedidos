# Sistema de Atendimento e Consulta de Pedidos

Aplicação web para atendimento conversacional e consulta do status de pedidos.

O sistema combina uma interface de conversação com uma rotina específica para localizar pedidos em uma base de dados e apresentar seu status.

## Funcionalidades

- Conversação por interface web;
- manutenção do contexto recente da conversa;
- identificação de solicitações relacionadas a pedidos;
- consulta de pedidos por número;
- apresentação do status do pedido;
- tratamento de pedidos inexistentes;
- botão para iniciar uma nova conversa.

## Tecnologias

- Python
- Gradio
- PyTorch
- Hugging Face Transformers
- Pandas

## Estrutura

```text
sistema-atendimento-pedidos/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Requisitos

- Python 3.10 ou superior;
- conexão com a internet na primeira execução para obter os arquivos necessários do modelo.

## Instalação

Clone o repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
cd sistema-atendimento-pedidos
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Inicie a aplicação:

```bash
python app.py
```

O endereço da aplicação será apresentado no terminal.

## Consulta de pedidos

A aplicação utiliza uma base de demonstração com os seguintes registros:

| Número do pedido | Status |
|---|---|
| 12345 | Shipped |
| 67890 | Processing |
| 11121 | Delivered |
| 22232 | Cancelled |

Exemplo de consulta:

```text
check my order
```

Em seguida, informe o número do pedido:

```text
12345
```

## Organização do código

O projeto separa as principais responsabilidades em funções:

- `carregar_modelo()` realiza a inicialização do modelo;
- `verificar_status_pedido()` consulta a base de pedidos;
- `responder()` processa a conversação;
- `processar_entrada()` controla o fluxo da interface;
- `limpar_conversa()` reinicia o atendimento.

O modelo é carregado uma única vez durante a inicialização da aplicação. A geração das respostas utiliza um limite de novos tokens e mantém apenas o contexto recente da conversa.

## Próximas evoluções

- substituição da base de demonstração por uma fonte de dados persistente;
- suporte a diferentes operações de atendimento;
- melhoria da identificação das solicitações;
- internacionalização da interface;
- autenticação de usuários;
- publicação da aplicação em ambiente de hospedagem.

## Licença

Este projeto está disponível sob a licença MIT.
