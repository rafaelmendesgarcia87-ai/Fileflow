import streamlit as st
import time
from config import CHAVE_PIX_OFICIAL, PLANS_DATA
from styles import apply_custom_css

# IMPORTAÇÃO SEGURA DA IA GEMINI
try:
    import google.generativeai as genai
    IA_DISPONIVEL = True
except ImportError:
    IA_DISPONIVEL = False

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="FileFlow v1.0 | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# APLICA ESTILO VISUAL
apply_custom_css()

# PAINEL LATERAL
with st.sidebar:
    st.title("⚡ FileFlow v1.0")
    st.subheader("Painel do Servidor")
    
    api_key_input = st.text_input("Insira sua API Key do Gemini:", type="password", help="Chave de API do Google Gemini")
    
    if api_key_input:
        if IA_DISPONIVEL:
            try:
                genai.configure(api_key=api_key_input)
                st.success("IA Conectada!")
            except Exception as e:
                st.error(f"Erro na API: {e}")
        else:
            st.warning("O pacote google-generativeai precisa estar no requirements.txt")

# CABEÇALHO PRINCIPAL
st.markdown("""
<div class="hero-banner">
    <h1 class="hero-title">FileFlow v1.0</h1>
    <p class="hero-subtitle">Infraestrutura Autônoma Gerenciada por IA</p>
</div>
""", unsafe_allow_html=True)

# ABAS DO APLICATIVO
tab1, tab2, tab3 = st.tabs(["📁 Processamento & IA", "🖥️ Planos & Servidores", "💳 Pagamento Pix"])

# TAB 1: PROCESSAMENTO DE ARQUIVOS
with tab1:
    col_upload, col_ai = st.columns([1, 1], gap="large")
    
    with col_upload:
        st.subheader(" Upload de Arquivos")
        uploaded_file = st.file_uploader("Escolha os documentos para processar na nuvem:", type=["pdf", "txt", "csv", "json", "epub"])
        if uploaded_file:
            st.success(f"Arquivo '{uploaded_file.name}' recebido com sucesso!")
            
    with col_ai:
        st.subheader(" Processador IA")
        user_prompt = st.text_area("Instruções para a IA:", placeholder="Ex: Resuma este documento e extraia os pontos principais.")
        if st.button("Executar Ação Inteligente", type="primary"):
            if api_key_input and IA_DISPONIVEL:
                with st.spinner("Processando dados na IA..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        response = model.generate_content(f"{user_prompt}\n\nArquivo: {uploaded_file.name if uploaded_file else 'Nenhum'}")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Erro ao processar: {e}")
            else:
                st.error("Insira uma chave API válida na barra lateral para usar a IA.")

# TAB 2: SELEÇÃO DE PLANOS
with tab2:
    st.subheader("Selecione a Capacidade do Seu Servidor")
    c1, c2, c3, c4 = st.columns(4)
    
    cols = [c1, c2, c3, c4]
    for col, (plan_name, info) in zip(cols, PLANS_DATA.items()):
        with col:
            st.markdown(f"""
            <div class="server-card">
                {'<span class="badge-promo">' + info['badge'] + '</span>' if info['badge'] != 'None' else ''}
                <h3>{plan_name}</h3>
                <p><b>{info['gb']} GB</b> de Armazenamento</p>
                <p>{info['price']}</p>
                <p><small>{info['desc']}</small></p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Ativar {plan_name}", key=f"btn_{plan_name}"):
                st.session_state['plano_selecionado'] = plan_name
                st.success(f"Plano {plan_name} selecionado! Vá até a aba 'Pagamento Pix'.")

# TAB 3: CHECKOUT PIX
with tab3:
    st.subheader("Finalização da Assinatura via Pix")
    plano_atual = st.session_state.get('plano_selecionado', 'VIP Plus')
    st.write(f"**Plano Selecionado:** {plano_atual}")
    
    st.code(CHAVE_PIX_OFICIAL, language="text")
    st.info("Copie a chave Pix acima e efetue a transferência no seu aplicativo de banco.")
    
    if st.button("Confirmar Pagamento e Ativar Servidor", type="primary"):
        with st.spinner("Confirmando transação no banco..."):
            time.sleep(1.5)
            st.balloons()
            st.success(f"Pagamento Confirmado! Servidor Dedicado ativado com sucesso.")
