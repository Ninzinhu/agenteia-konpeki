
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Configura o título da página e o modelo a ser usado
st.set_page_config(page_title="Chat com Llama 3", page_icon="🤖")
st.title("Chatbot com Llama 3 via Ollama")

# Inicializa o modelo de chat da LangChain, conectando ao Ollama
# Certifique-se de que o Ollama está rodando com o modelo 'llama3'
llm = ChatOllama(model="llama3")

# Inicializa o histórico da conversa na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens do histórico na interface
for message in st.session_state.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# Captura a entrada do usuário
if prompt := st.chat_input("Qual a sua pergunta?"):
    # Adiciona a mensagem do usuário ao histórico e à interface
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("human"):
        st.markdown(prompt)

    # Gera e exibe a resposta do modelo
    with st.chat_message("ai"):
        with st.spinner("Pensando..."):
            # Envia todo o histórico para o modelo
            response = llm.invoke(st.session_state.messages)
            st.markdown(response.content)
    
    # Adiciona a resposta do modelo ao histórico
    st.session_state.messages.append(AIMessage(content=response.content))
