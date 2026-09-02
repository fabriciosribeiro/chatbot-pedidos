# Chatbot com IA e Consulta de Status de Pedidos

Projeto de chatbot desenvolvido em Python utilizando o modelo **microsoft/DialoGPT-medium**, com duas funcionalidades principais:

- conversação livre utilizando um modelo de linguagem;
- consulta de status de pedidos a partir de uma pequena base de dados em Pandas.

O projeto foi desenvolvido inicialmente como atividade prática de Inteligência Artificial e posteriormente organizado e corrigido para compor um portfólio de projetos.

## Funcionalidades

### 1. Conversação livre

O chatbot utiliza o **DialoGPT-medium** para gerar respostas a partir do histórico da conversa.

### 2. Consulta de pedidos

Quando o usuário solicita informações sobre um pedido, o sistema identifica a intenção por meio de palavras-chave e solicita o número do pedido.

A base de demonstração contém os seguintes pedidos:

| Número | Status |
|---|---|
| 12345 | Shipped |
| 67890 | Processing |
| 11121 | Delivered |
| 22232 | Cancelled |

### 3. Controle da geração

O notebook utiliza `max_new_tokens=50` para limitar o tamanho das respostas e evitar gerações excessivamente longas.

Também foram implementados:

- `torch.no_grad()` durante a inferência;
- modelo carregado uma única vez;
- modelo colocado em modo de avaliação;
- limitação do histórico da conversa a 800 tokens;
- tratamento de entradas vazias;
- consulta de pedidos sem uso de exceções genéricas.

## Tecnologias

- Python
- PyTorch
- Hugging Face Transformers
- Pandas
- Jupyter Notebook

## Modelo utilizado

**microsoft/DialoGPT-medium**

https://huggingface.co/microsoft/DialoGPT-medium

> **Observação:** o DialoGPT é um modelo voltado principalmente para conversação em inglês. Portanto, esta versão do projeto mantém o modelo original utilizado na atividade. Uma evolução posterior do projeto poderá utilizar um modelo otimizado para português brasileiro.

## Estrutura do projeto

```text
chatbot-pedidos/
├── chatbot_pedidos.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd chatbot-pedidos
```

### 2. Crie um ambiente virtual

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

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o notebook

Abra:

```text
chatbot_pedidos.ipynb
```

e execute as células em sequência.

Na primeira execução, o Transformers fará o download do modelo `microsoft/DialoGPT-medium`.

## Exemplos

### Conversação

```text
You: hi
Bot: ...
```

### Consulta de pedido

```text
You: I want to check my order
Could you please enter your order number? 12345
Bot: The status of your order 12345 is: Shipped
```

### Encerramento

```text
You: exit
Bot: Goodbye!
```

## Evolução planejada

Este projeto representa uma primeira versão funcional de um chatbot baseado em modelo de linguagem.

Como evolução do projeto, pretende-se:

- substituir o modelo por uma alternativa com melhor desempenho em português brasileiro;
- desenvolver uma interface web com Gradio;
- separar a lógica do chatbot da interface;
- transformar a base de pedidos em uma fonte de dados externa;
- melhorar a identificação de intenções;
- disponibilizar a aplicação no Hugging Face Spaces;
- adicionar uma arquitetura mais próxima de uma aplicação real de atendimento.

## Créditos

Projeto baseado em uma atividade prática de Inteligência Artificial, posteriormente revisada e organizada para fins de estudo e portfólio.

Modelo utilizado: **DialoGPT-medium**, da Microsoft.

## Licença

Este projeto é disponibilizado sob a licença MIT para fins educacionais e de portfólio.
