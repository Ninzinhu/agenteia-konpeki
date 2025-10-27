
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Konpeki",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- LÓGICA DO CHAT ---

# Função para gerar a resposta em streaming
def get_response_stream(user_prompt, chat_history):
    # Adiciona a pergunta do usuário ao histórico para enviar ao modelo
    messages = chat_history + [HumanMessage(content=user_prompt)]
    
    # Retorna o gerador de streaming
    return llm.stream(messages)

# Tenta inicializar o modelo de chat
try:
    llm = ChatOllama(model="llama3")
except Exception as e:
    st.error(f"Erro ao conectar com o Ollama: {e}")
    st.info("Certifique-se de que o Ollama está em execução e o modelo 'llama3' foi baixado com 'ollama pull llama3'.")
    st.stop()

# --- INTERFACE DO USUÁRIO (UI) ---

st.title("Konpeki 💎")

# Barra Lateral
with st.sidebar:
    st.header("Opções")
    if st.button("Limpar conversa com Konpeki"):
        # Reinicia o histórico, mantendo o prompt do sistema
        st.session_state.messages = [st.session_state.system_prompt, AIMessage(content="Olá! Eu sou Konpeki. Como posso te ajudar hoje?")]
        st.rerun()

# Define o prompt do sistema que dá a personalidade à IA
# Este prompt é enviado ao modelo, mas não é exibido no chat
system_prompt = SystemMessage(content="Você é Konpeki, uma assistente de IA. Seu nome significa 'azul-celeste profundo' em japonês. Você é prestativa, inteligente e formal. Sempre se apresente como Konpeki na sua primeira saudação.")
st.session_state.system_prompt = system_prompt

# Inicializa o histórico da conversa se ainda não existir
if "messages" not in st.session_state:
    st.session_state.messages = [system_prompt, AIMessage(content="Olá! Eu sou Konpeki. Como posso te ajudar hoje?")]

# Exibe as mensagens do histórico (pulando o prompt do sistema)
for message in st.session_state.messages:
    if isinstance(message, SystemMessage):
        continue
    avatar = "💎" if isinstance(message, AIMessage) else "👤"
    with st.chat_message(message.type, avatar=avatar):
        st.markdown(message.content)

# Captura a entrada do usuário
if prompt := st.chat_input("Converse com a Konpeki..."):
    # Adiciona e exibe a mensagem do usuário
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("human", avatar="👤"):
        st.markdown(prompt)

    # Gera e exibe a resposta da IA em streaming
    with st.chat_message("ai", avatar="💎"):
        response_stream = get_response_stream(prompt, st.session_state.messages)
        full_response = st.write_stream(response_stream)
    
    # Adiciona a resposta completa da IA ao histórico
    st.session_state.messages.append(AIMessage(content=full_response))
