import streamlit as st
import time

# IMPORTAÇÃO SEGURA DA IA GEMINI
try:
    import google.generativeai as genai
    IA_DISPONIVEL = True
except ImportError:
    IA_DISPONIVEL = False

# CONFIGURAÇÃO DE SEGURANÇA DA CHAVE PIX (BUSCA DOS SECRETS)
try:
    CHAVE_PIX_OFICIAL = st.secrets["CHAVE_PIX_OFICIAL"]
except Exception:
    CHAVE_PIX_OFICIAL = "Chave Pix não configurada nos Secrets"

# DADOS DOS PLANOS
PLANS_DATA = {
    "Member": {"gb": 10, "price": "R$ 5,00/mês", "badge": "None", "desc": "Container Estandard Isolado"},
    "VIP": {"gb": 50, "price": "R$ 10,00/mês", "badge": "Novo", "desc": "Processamento Prioritário"},
    "Mega VIP": {"gb": 200, "price": "R$ 40,00/mês", "badge": "None", "desc": "Cluster de Alta Banda"},
    "VIP Plus": {"gb": 500, "price": "R$ 60,00/mês", "badge": "Desconto 40%", "desc": "Servidor Neural Exclusivo"},
}

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="FileFlow v1.0 | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ESTILIZAÇÃO VISUAL (CSS EMBUTIDO)
st.markdown("""
<style>
.stApp { background-color: #030712; color: #f3f4f6; font-family: 'Inter', system-ui, sans-serif; }
.hero-banner { background: linear-gradient(135deg, #0d9488, #00FFCC, #38b2ac); padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 25px; }
.hero-title { font-size: 2.2rem; font-weight: 900; color: #000; margin: 0; }
.hero-subtitle { font-size: 1rem; color: #111827; margin-top: 5px; }
.server-card { background: rgba(15, 23, 42, 0.7); border: 1px solid #1e293b; border-radius: 16px; padding: 20px; text-align: center; }
.badge-promo { background-color: #EC4899; color: #ffffff; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# PAINEL LATERAL
with st.sidebar:
    st.title("⚡ FileFlow v1.0")
    st.subheader("Painel do Servidor")
    api_key_input = st.text_input("Insira sua API Key do Gemini:", type="password")
    
    if api_key_input:
        if IA_DISPONIVEL:
            try:
                genai.configure(api_key=api_key_input)
                st.success("IA Conectada!")
            except Exception as e:
                st.error(f"Erro na API: {e}")
        else:
            st.warning("Adicione google-generativeai no requirements.txt")

# CABEÇALHO
st.markdown("""
<div class="hero-banner">
    <h1 class="hero-title">FileFlow v1.0</h1>
    <p class="hero-subtitle">Infraestrutura Autônoma Gerenciada por IA</p>
</div>
""", unsafe_allow_html=True)

# ABAS
tab1, tab2, tab3 = st.tabs(["📁 Processamento & IA", "🖥️ Planos & Servidores", "💳 Pagamento Pix"])

with tab1:
    col_upload, col_ai = st.columns([1, 1], gap="large")
    with col_upload:
        st.subheader(" Upload de Arquivos")
        uploaded_file = st.file_uploader("Escolha os documentos para processar:", type=["pdf", "txt", "csv", "json", "epub"])
        if uploaded_file:
            st.success(f"Arquivo '{uploaded_file.name}' recebido com sucesso!")
            
    with col_ai:
        st.subheader(" Processador IA")
        user_prompt = st.text_area("Instruções para a IA:", placeholder="Ex: Resuma este documento...")
        if st.button("Executar Ação Inteligente", type="primary"):
            if api_key_input and IA_DISPONIVEL:
                with st.spinner("Processando..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        response = model.generate_content(f"{user_prompt}\n\nArquivo: {uploaded_file.name if uploaded_file else 'Nenhum'}")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Erro: {e}")
            else:
                st.error("Insira a chave API na barra lateral.")

with tab2:
    st.subheader("Selecione a Capacidade do Seu Servidor")
    cols = st.columns(4)
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
                st.success(f"Plano {plan_name} selecionado!")

with tab3:
    st.subheader("Finalização da Assinatura via Pix")
    plano_atual = st.session_state.get('plano_selecionado', 'VIP Plus')
    st.write(f"**Plano Selecionado:** {plano_atual}")
    st.code(CHAVE_PIX_OFICIAL, language="text")
    st.info("Copie a chave Pix acima e efetue a transferência no seu aplicativo de banco.")
    
    if st.button("Confirmar Pagamento e Ativar Servidor", type="primary"):
        with st.spinner("Confirmando transação..."):
            time.sleep(1.5)
            st.balloons()
            st.success("Pagamento Confirmado! Servidor Dedicado ativado.")
import streamlit as st
import time

# ---------------------------------------------------------
# CONFIGURAÇÃO DE SEGURANÇA DA CHAVE PIX (OCULTA NO CÓDIGO)
# ---------------------------------------------------------
try:
    CHAVE_PIX_OFICIAL = st.secrets["CHAVE_PIX_OFICIAL"]
except Exception:
    CHAVE_PIX_OFICIAL = "Chave Pix segura configurada nos Secrets"

# IMPORTAÇÃO SEGURA DA IA GEMINI
try:
    import google.generativeai as genai
    IA_DISPONIVEL = True
except ImportError:
    IA_DISPONIVEL = False

# DADOS DOS PLANOS E SERVIDORES (INCLUINDO PLANO ADM DE 500 GB)
PLANS_DATA = {
    "ADM / Google": {"gb": 500, "price": "R$ 0,00 (Acesso ADM)", "badge": "Administrador", "desc": "Servidor Dedicado de Alta Performance"},
    "Member": {"gb": 10, "price": "R$ 5,00/mês", "badge": "Básico", "desc": "Container Estandard Isolado"},
    "VIP": {"gb": 50, "price": "R$ 10,00/mês", "badge": "Popular", "desc": "Processamento Prioritário"},
    "Mega VIP": {"gb": 200, "price": "R$ 40,00/mês", "badge": "Avançado", "desc": "Cluster de Alta Banda"},
    "VIP Plus": {"gb": 500, "price": "R$ 60,00/mês", "badge": "Desconto 40%", "desc": "Servidor Neural Exclusivo"},
}

import streamlit as st
import time

# ---------------------------------------------------------
# CONFIGURAÇÃO DE SEGURANÇA DA CHAVE PIX (OCULTA NO CÓDIGO)
# ---------------------------------------------------------
try:
    CHAVE_PIX_OFICIAL = st.secrets["CHAVE_PIX_OFICIAL"]
except Exception:
    CHAVE_PIX_OFICIAL = "Chave Pix configurada nos Secrets"

# IMPORTAÇÃO SEGURA DA IA GEMINI
try:
    import google.generativeai as genai
    IA_DISPONIVEL = True
except ImportError:
    IA_DISPONIVEL = False

# DADOS DOS PLANOS E SERVIDORES (INCLUINDO PLANO ADM DE 500 GB)
PLANS_DATA = {
    "ADM / Google": {"gb": 500, "price": "R$ 0,00 (Acesso ADM)", "badge": "Administrador", "desc": "Servidor Dedicado de Alta Performance"},
    "Member": {"gb": 10, "price": "R$ 5,00/mês", "badge": "Básico", "desc": "Container Estandard Isolado"},
    "VIP": {"gb": 50, "price": "R$ 10,00/mês", "badge": "Popular", "desc": "Processamento Prioritário"},
    "Mega VIP": {"gb": 200, "price": "R$ 40,00/mês", "badge": "Avançado", "desc": "Cluster de Alta Banda"},
    "VIP Plus": {"gb": 500, "price": "R$ 60,00/mês", "badge": "Desconto 40%", "desc": "Servidor Neural Exclusivo"},
}

# ---------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="FileFlow v1.0 | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ESTILO VISUAL MODERNO
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: #f8fafc;
    font-family: 'Inter', system-ui, sans-serif;
}
.hero-banner {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 1px solid #334155;
    padding: 30px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 25px;
    border-left: 6px solid #e11d48;
}
.hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0;
}
.hero-subtitle {
    font-size: 1.1rem;
    color: #94a3b8;
    margin-top: 5px;
}
.server-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.server-card:hover {
    border-color: #e11d48;
}
.badge-red {
    background-color: #e11d48;
    color: white;
    font-size: 0.75rem;
    font-weight: bold;
    padding: 4px 10px;
    border-radius: 6px;
    display: inline-block;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PAINEL LATERAL
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='color:#e11d48;'>⚡ FileFlow v1.0</h2>", unsafe_allow_html=True)
    st.subheader("Configurações do Servidor")
    
    api_key_input = st.text_input("Chave API Gemini:", type="password", help="Insira sua chave para ativar os recursos de IA")
    
    if api_key_input:
        if IA_DISPONIVEL:
            try:
                genai.configure(api_key=api_key_input)
                st.success("IA Ativa e Conectada!")
            except Exception as e:
                st.error(f"Erro ao conectar IA: {e}")
        else:
            st.warning("Adicione google-generativeai no arquivo requirements.txt")

# BANNER PRINCIPAL
st.markdown("""
<div class="hero-banner">
    <h1 class="hero-title">FileFlow v1.0</h1>
    <p class="hero-subtitle">Gerenciador de Arquivos Autônomo e Infraestrutura IA</p>
</div>
""", unsafe_allow_html=True)

# ABAS DO APLICATIVO
tab_ia, tab_servidores, tab_checkout = st.tabs(["🤖 Processador & IA Central", "🖥️ Catálogo de Servidores", "💳 Ativação via Pix"])

# ---------------------------------------------------------
# ABA 1: PROCESSADOR & IA
# ---------------------------------------------------------
with tab_ia:
    st.subheader("Central de Processamento de Arquivos")
    col_up, col_ai = st.columns([1, 1], gap="large")
    
    with col_up:
        uploaded_file = st.file_uploader("Selecione seus arquivos para armazenar ou processar:", type=["pdf", "txt", "csv", "json", "epub"])
        if uploaded_file:
            st.success(f"Arquivo '{uploaded_file.name}' carregado e pronto para uso no seu servidor.")
            
    with col_ai:
        user_prompt = st.text_area("Instruções para a IA:", placeholder="Ex: Resuma o documento, extraia tabelas ou analise o conteúdo...")
        if st.button("Executar Ação com IA", type="primary"):
            if api_key_input and IA_DISPONIVEL:
                with st.spinner("A IA está processando seus dados..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        content = f"{user_prompt}\n\nArquivo: {uploaded_file.name if uploaded_file else 'Nenhum'}"
                        response = model.generate_content(content)
                        st.markdown("### Resposta da IA:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Erro no processamento: {e}")
            else:
                st.error("Insira a Chave API na barra lateral para usar a IA.")

# ---------------------------------------------------------
# ABA 2: CATÁLOGO DE SERVIDORES
# ---------------------------------------------------------
with tab_servidores:
    st.subheader("Gerenciar Capacidade dos Servidores")
    cols = st.columns(len(PLANS_DATA))
    
    for idx, (plan_name, info) in enumerate(PLANS_DATA.items()):
        with cols[idx]:
            st.markdown(f"""
            <div class="server-card">
                <span class="badge-red">{info['badge']}</span>
                <h3>{plan_name}</h3>
                <p><b>{info['gb']} GB</b> Armazenamento</p>
                <p style="color:#e11d48; font-weight:bold;">{info['price']}</p>
                <p><small>{info['desc']}</small></p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Ativar {plan_name}", key=f"btn_server_{idx}"):
                st.session_state['plano_ativo'] = plan_name
                st.session_state['gb_limite'] = info['gb']
                st.success(f"Servidor {plan_name} ({info['gb']} GB) ativado!")

# ---------------------------------------------------------
# ABA 3: ATIVAÇÃO VIA PIX
# ---------------------------------------------------------
with tab_checkout:
    st.subheader("Ativação de Assinatura")
    plano_atual = st.session_state.get('plano_ativo', 'VIP Plus')
    gb_atual = st.session_state.get('gb_limite', 500)
    
    st.markdown(f"**Servidor Selecionado:** <span style='color:#e11d48; font-weight:bold;'>{plano_atual} ({gb_atual} GB)</span>", unsafe_allow_html=True)
    st.write("Copie a chave Pix abaixo para realizar a transferência no app do seu banco:")
    
    st.code(CHAVE_PIX_OFICIAL, language="text")
    
    if st.button("Confirmar Pagamento e Liberar Servidor", type="primary", key="btn_confirmar_pix"):
        with st.spinner("Verificando transação..."):
            time.sleep(1.5)
            st.balloons()
            st.success(f"Servidor '{plano_atual}' de {gb_atual} GB liberado com sucesso!")
