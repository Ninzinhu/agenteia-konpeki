
# Konpeki 💎 - Assistente de IA Pessoal

Konpeki (紺碧, "azul-celeste profundo") é um projeto de assistente de IA que roda localmente, garantindo total privacidade dos dados e sem custos de API. Ele utiliza um modelo de linguagem de código aberto (LLM) através do Ollama e apresenta uma interface de chat amigável construída com Streamlit.

## ✨ Funcionalidades

- **Interface de Chat Interativa:** Uma interface web simples e intuitiva para conversar com a IA.
- **Respostas em Tempo Real:** As respostas da IA são exibidas palavra por palavra (streaming), proporcionando uma experiência dinâmica.
- **Personalidade Definida:** A IA possui uma identidade predefinida ("Konpeki") através de um prompt de sistema, que pode ser customizado.
- **Gerenciamento de Histórico:** O histórico da conversa é mantido durante a sessão e pode ser limpo através de um botão na barra lateral.
- **100% Local e Privado:** Utiliza o Ollama para rodar o modelo de linguagem na sua própria máquina. Nenhuma informação é enviada para serviços de terceiros.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit:** Para a criação da interface web.
- **LangChain:** Como framework para orquestrar a lógica do agente de IA.
- **Ollama:** Para servir o modelo de linguagem de código aberto localmente.
- **Llama 3:** O modelo de linguagem (LLM) que atua como o "cérebro" da Konpeki.

---

## 🚀 Guia de Instalação e Execução

Siga estes passos para configurar e rodar o projeto na sua máquina.

### Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

1.  **Python:** [Instale a partir do site oficial](https://www.python.org/downloads/).
2.  **Ollama:** [Instale a partir do site oficial](https://ollama.com/).

### Passo 1: Baixar o Modelo de Linguagem

Após instalar o Ollama, abra o seu terminal e rode o seguinte comando para baixar o modelo Llama 3. Este passo pode demorar um pouco dependendo da sua conexão com a internet.

```bash
ollama pull llama3
```

*Opcional: Após o download, você pode rodar `ollama run llama3` no terminal para ter uma primeira conversa com o modelo puro e garantir que ele está funcionando.*

### Passo 2: Configurar o Ambiente do Projeto

1.  **Navegue até a pasta do projeto:**
    ```bash
    cd caminho/para/agente-ia-konpeki
    ```

2.  **(Recomendado) Crie e ative um ambiente virtual:**
    Isso isola as dependências do projeto e evita conflitos.
    ```bash
    # Criar o ambiente
    python3 -m venv venv

    # Ativar no Linux/macOS
    source venv/bin/activate

    # Ativar no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as bibliotecas Python necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

### Passo 3: Executar a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, inicie a aplicação Streamlit com o comando:

```bash
streamlit run app.py
```

Uma nova aba deve abrir automaticamente no seu navegador, exibindo a interface de chat da Konpeki. Se não abrir, o terminal mostrará um endereço local (ex: `http://localhost:8501`) que você pode abrir manualmente.

**Importante:** O servidor do Ollama precisa estar em execução para que o `app.py` funcione. Normalmente, o Ollama roda em segundo plano após a instalação. Se a aplicação mostrar um erro de conexão, certifique-se de que o aplicativo do Ollama está aberto.

---

## 🧠 Como Funciona?

- **Frontend (Streamlit):** O arquivo `app.py` usa a biblioteca Streamlit para desenhar a interface de chat, incluindo a barra lateral, os avatares e as mensagens.
- **Lógica de Chat (LangChain):** A biblioteca LangChain é usada para estruturar a conversa. Ela gerencia o histórico de mensagens (incluindo o prompt de sistema secreto que define a personalidade) e se comunica com o modelo de linguagem.
- **"Cérebro" (Ollama + Llama 3):** Quando você envia uma pergunta, o LangChain a envia para o servidor Ollama, que por sua vez a processa com o modelo Llama 3 e devolve a resposta. Todo esse processo acontece na sua máquina.

## 🔮 Próximos Passos

A próxima grande melhoria para a Konpeki é dar a ela conhecimento sobre seus próprios dados. Isso é feito através de uma técnica chamada **RAG (Retrieval-Augmented Generation)**, que permite que a IA consulte seus documentos (PDFs, TXTs, etc.) para formular respostas.
