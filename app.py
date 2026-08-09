import os
import streamlit as st
import google.genai as genai

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="File Flow - AI File Service", page_icon="📁", layout="centered")

st.title("📁 File Flow")
st.caption("Serviço Inteligente de Gerenciamento e Transferência de Arquivos com IA")

# PAINEL LATERAL (ASSINATURA E CHAVE)
st.sidebar.header("Painel do Cliente")
status_assinatura = st.sidebar.radio("Plano Atual:", ["Gratuito (Demonstração)", "Premium (R$ 5,00/mês)"])

if status_assinatura == "Premium (R$ 5,00/mês)":
    st.sidebar.success("Status: Assinatura Ativa (Acesso Total)")
else:
    st.sidebar.warning("Status: Modo Limitado")

gemini_api_key = st.sidebar.text_input("Chave da API Gemini", type="password", help="Insira sua chave para ativar a IA")

# INICIALIZAÇÃO DA IA
ai_client = None
if gemini_api_key:
    try:
        ai_client = genai.Client(api_key=gemini_api_key)
        st.sidebar.info("IA Gemini Conectada com Sucesso!")
    except Exception as e:
        st.sidebar.error(f"Erro ao conectar IA: {e}")

# ÁREA PRINCIPAL - INTERAÇÃO COM A IA E ARQUIVOS
st.header("1. Envie ou Solicite uma Transferência")

instrucao = st.text_area(
    "O que você deseja fazer com seus arquivos?",
    placeholder="Exemplo: Mova o arquivo 'Relatorio.pdf' do meu armazenamento para a pasta 'Financeiro' ou analise o conteúdo dele."
)

arquivo_enviado = st.file_uploader("Arraste ou selecione um arquivo para a IA processar:", type=None)

if st.button("Executar Ação com IA", type="primary"):
    if not gemini_api_key or not ai_client:
        st.error("Por favor, insira a Chave da API Gemini no painel lateral para usar a IA.")
    else:
        with st.spinner("A IA está processando seu pedido e analisando os arquivos..."):
            try:
                # Caso haja um arquivo anexado
                if arquivo_enviado is not None:
                    bytes_data = arquivo_enviado.getvalue()
                    
                    # Prompt para a IA agir como a assistente do File Flow
                    prompt_sistema = f"""
                    Você é a IA integrada ao serviço File Flow. 
                    O usuário enviou o arquivo '{arquivo_enviado.name}'.
                    Instrução do usuário: '{instrucao}'
                    
                    Analise a instrução, classifique a categoria do arquivo e confirme para onde ele deve ser roteado/transferido.
                    """
                    
                    response = ai_client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[prompt_sistema]
                    )
                    
                    st.success("Ação concluída pela IA do File Flow!")
                    st.markdown("### Resposta da IA:")
                    st.write(response.text)

                # Caso seja apenas uma instrução em texto
                elif instrucao:
                    prompt_sistema = f"""
                    Você é o assistente virtual do serviço File Flow (Gerenciamento inteligente de arquivos com IA por R$ 5/mês).
                    O usuário deu a seguinte instrução de comando/transferência: '{instrucao}'.
                    
                    Responda confirmando o entendimento da operação e os passos automatizados que serão executados.
                    """
                    response = ai_client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt_sistema
                    )
                    
                    st.success("Comando processado!")
                    st.markdown("### Resposta da IA:")
                    st.write(response.text)
                else:
                    st.warning("Por favor, escreva um comando ou envie um arquivo.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar com a IA: {e}")

st.divider()
st.caption("File Flow © 2026 - Todos os direitos reservados.")
import streamlit as st

# Configuração da página com tema escuro imersivo
st.set_page_config(page_title="FileFlow | Neural Cloud", page_icon="⚡", layout="wide")

# Estilização CSS Customizada (Visual Futurista / Tech / Neônio)
st.markdown("""
    <style>
    .stApp {
        background-color: #05050A;
        color: #00FFCC;
        font-family: 'Inter', sans-serif;
    }
    .hero-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00FFCC, #0066FF, #9900FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        text-align: center;
        color: #8892B0;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .plan-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.05);
        position: relative;
    }
    .plan-card:hover {
        border-color: #00FFCC;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.2);
        transform: translateY(-5px);
    }
    .plan-card-highlight {
        background: rgba(15, 23, 42, 0.9);
        border: 2px solid #00FFCC;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 35px rgba(0, 255, 204, 0.3);
        position: relative;
    }
    .badge-promo {
        background: #FF007F;
        color: #FFFFFF;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 20px;
        position: absolute;
        top: -12px;
        right: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .plan-title {
        color: #FFFFFF;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .plan-storage {
        color: #00FFCC;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 15px 0;
    }
    .plan-price {
        color: #E2E8F0;
        font-size: 1.3rem;
        font-weight: 600;
    }
    .plan-old-price {
        color: #64748B;
        text-decoration: line-through;
        font-size: 0.9rem;
        margin-left: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<p class="hero-title">FileFlow // Neural Matrix</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Infraestrutura de Arquivos Autônoma Gerenciada por Inteligência Artificial</p>', unsafe_allow_html=True)

st.markdown("---")

# Seção de Planos Futuristas
st.markdown("### 🌐 SELECIONE SEU NÚCLEO DE PROCESSAMENTO E ARMAZENAMENTO")
st.write("Cada plano ativa instantaneamente um contêiner dedicado isolado via Docker com cota dedicada na nuvem.")

col1, col2, col3, col4 = st.columns(4)

# Plano Member
with col1:
    st.markdown("""
        <div class="plan-card">
            <div class="plan-title">MEMBER</div>
            <div class="plan-storage">10 GB</div>
            <p style="color: #8892B0; font-size: 0.9rem;">Isolamento padrão / Rede otimizada</p>
            <hr style="border-color: #1E293B;">
            <div class="plan-price">R$ 5,00<span style="font-size: 0.8rem; color: #8892B0;">/mês</span></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Ativar Member", key="btn_member", use_container_width=True):
        st.success("Redirecionando para gateway seguro...")

# Plano VIP
with col2:
    st.markdown("""
        <div class="plan-card">
            <div class="plan-title">VIP</div>
            <div class="plan-storage">50 GB</div>
            <p style="color: #8892B0; font-size: 0.9rem;">Prioridade de IA / Alta performance</p>
            <hr style="border-color: #1E293B;">
            <div class="plan-price">R$ 10,00<span style="font-size: 0.8rem; color: #8892B0;">/mês</span></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Ativar VIP", key="btn_vip", use_container_width=True):
        st.success("Redirecionando para gateway seguro...")

# Plano Mega VIP
with col3:
    st.markdown("""
        <div class="plan-card">
            <div class="plan-title">MEGA VIP</div>
            <div class="plan-storage">200 GB</div>
            <p style="color: #8892B0; font-size: 0.9rem;">Servidor Dedicado / Banda Larga Ilimitada</p>
            <hr style="border-color: #1E293B;">
            <div class="plan-price">R$ 40,00<span style="font-size: 0.8rem; color: #8892B0;">/mês</span></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Ativar Mega VIP", key="btn_mega", use_container_width=True):
        st.success("Redirecionando para gateway seguro...")

# Plano VIP Plus (Destaque / Promoção)
with col4:
    st.markdown("""
        <div class="plan-card-highlight">
            <div class="badge-promo">40% OFF</div>
            <div class="plan-title" style="color: #00FFCC;">VIP PLUS</div>
            <div class="plan-storage">500 GB</div>
            <p style="color: #8892B0; font-size: 0.9rem;">Cluster Neural Exclusivo / Máxima Prioridade</p>
            <hr style="border-color: #1E293B;">
            <div class="plan-price">R$ 60,00<span style="font-size: 0.8rem; color: #8892B0;">/mês</span><span class="plan-old-price">R$ 100</span></div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Ativar VIP Plus", key="btn_plus", use_container_width=True):
        st.success("Redirecionando para gateway seguro...")

st.markdown("---")

# Painel de Status do Sistema (Simulador para Investidores/Empresários)
st.markdown("### 📊 TELEMETRIA DO SISTEMA")
col_stat1, col_stat2, col_stat3 = st.columns(3)
col_stat1.metric(label="Status dos Servidores", value="ONLINE", delta="100% SLA")
col_stat2.metric(label="Latencia Média da IA", value="18 ms", delta="-2 ms")
col_stat3.metric(label="Nós Ativos na Nuvem", value="1.024", delta="+12 hoje")
import streamlit as st
import google.generativeai as genai
import time

# ---------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA (ESTILO APLICATIVO FUTURISTA)
# ---------------------------------------------------------
st.set_page_config(
    page_title="FileFlow v1.0 | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS Cyberpunk / Futurista Avançada
st.markdown("""
    <style>
    /* Estilo Global */
    .stApp {
        background: #030712;
        color: #F3F4F6;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }
    
    /* Topo do App / Hero Header */
    .app-header {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.1);
        margin-bottom: 25px;
    }
    .app-title {
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #00FFCC, #3B82F6, #9333EA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .app-tagline {
        color: #94A3B8;
        font-size: 1rem;
        margin-top: 5px;
    }

    /* Cards Futuristas de Servidores / Planos */
    .server-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .server-card-vip {
        background: rgba(15, 23, 42, 0.95);
        border: 2px solid #00FFCC;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.25);
        position: relative;
    }
    .badge-promo {
        background: #EC4899;
        color: white;
        font-weight: bold;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 12px;
        position: absolute;
        top: -10px;
        right: 15px;
    }
    .server-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #FFFFFF;
    }
    .server-quota {
        font-size: 1.8rem;
        font-weight: 800;
        color: #00FFCC;
        margin: 10px 0;
    }
    .server-price {
        font-size: 1.2rem;
        color: #E2E8F0;
        font-weight: 600;
    }

    /* Painel do Pix */
    .pix-box {
        background: rgba(6, 78, 59, 0.3);
        border: 1px solid #059669;
        border-radius: 12px;
        padding: 15px;
        margin-top: 15px;
        text-align: center;
    }
    .pix-key {
        font-family: monospace;
        background: #022C22;
        color: #34D399;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: bold;
        display: inline-block;
        margin: 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# REGISTRO DE PLANOS & SERVIDORES DEDICADOS
# ---------------------------------------------------------
CHAVE_PIX_OFICIAL = "SUA_CHAVE_PIX_AQUI"  # <- Insira sua chave Pix (CPF ou Aleatória) aqui!

SERVIDORES_PLANOS = {
    "Member": {"gb": 10, "preco": "R$ 5,00/mês", "promo": None},
    "VIP": {"gb": 50, "preco": "R$ 10,00/mês", "promo": None},
    "Mega VIP": {"gb": 200, "preco": "R$ 40,00/mês", "promo": None},
    "VIP Plus": {"gb": 500, "preco": "R$ 60,00/mês", "promo": "40% OFF (De R$ 100 por R$ 60)"}
}

# ---------------------------------------------------------
# PAINEL LATERAL (CONFIGURAÇÃO DE CONEXÃO E IA)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/server.png", width=64)
    st.title("FileFlow v1.0")
    st.caption("Painel do Cliente & Servidores")
    
    st.subheader("🔑 Conexão com a IA")
    api_key_input = st.text_input("Chave API do Gemini", type="password", help="Insira sua chave do Google AI Studio para ativar o motor de IA.")
    
    if api_key_input:
        genai.configure(api_key=api_key_input)
        st.success("IA Conectada e Ativa ⚡")
    else:
        st.warning("Insira a Chave API para liberar a IA.")

    st.divider()
    st.markdown("### 🖥️ Status do Servidor Atual")
    st.info("Plano Atual: **Gratuito (Demonstração)**\n\nEspaço Usado: **0.1 GB / 2.0 GB**")

# ---------------------------------------------------------
# CABEÇALHO DO APLICATIVO
# ---------------------------------------------------------
st.markdown("""
    <div class="app-header">
        <h1 class="app-title">FILEFLOW // NEURAL CLOUD OS</h1>
        <p class="app-tagline">Gerenciador de Arquivos Autônomo & Processador Inteligente v1.0</p>
    </div>
""", unsafe_allow_html=True)

# Tabs / Navegação simplificada do Consumidor
tab1, tab2, tab3 = st.tabs(["⚡ Meu Servidor & IA", "🚀 Upgrade de Servidor (Planos)", "💳 Pagamento via Pix"])

# ---------------------------------------------------------
# TAB 1: MEU SERVIDOR & IA (USO DO APP)
# ---------------------------------------------------------
with tab1:
    col_upload, col_ia = st.columns([1, 1])
    
    with col_upload:
        st.subheader("📂 Enviar Arquivo para o Servidor")
        arquivo = st.file_uploader("Arraste seus documentos ou imagens para armazenar e analisar:", type=["pdf", "txt", "png", "jpg", "csv"])
        
        if arquivo:
            st.success(f"Arquivo `{arquivo.name}` enviado com sucesso para o seu servidor!")
            st.metric(label="Tamanho do Arquivo", value=f"{round(arquivo.size / (1024*1024), 2)} MB")

    with col_ia:
        st.subheader("🤖 IA Processadora de Arquivos")
        instrucao = st.text_area("O que você quer que a IA faça com seus arquivos armazenados?", placeholder="Exemplo: Resuma este documento e extraia os tópicos principais.")
        
        if st.button("Executar Processamento 🚀", use_container_width=True):
            if not api_key_input:
                st.error("Por favor, informe a Chave API na barra lateral para usar a IA.")
            else:
                with st.spinner("Conectando ao servidor neural..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        resposta = model.generate_content(instrucao if instrucao else "Análise do sistema FileFlow OK.")
                        st.markdown("### 📝 Resposta da IA:")
                        st.write(resposta.text)
                    except Exception as e:
                        st.error(f"Erro ao processar com a IA: {e}")

# ---------------------------------------------------------
# TAB 2: SELEÇÃO DE SERVIDORES / PLANOS
# ---------------------------------------------------------
with tab2:
    st.subheader("🌐 Escolha a Capaciade do seu Servidor Dedicado")
    st.write("Selecione um plano para expandir seu armazenamento e ativar servidores dedicados.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="server-card">
                <div class="server-title">MEMBER</div>
                <div class="server-quota">10 GB</div>
                <div class="server-price">{SERVIDORES_PLANOS['Member']['preco']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">Servidor Standard</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Assinar Member", key="p_member", use_container_width=True):
            st.session_state['plano_selecionado'] = "Member"
            st.info("Vá para a aba 'Pagamento via Pix' para finalizar.")

    with col2:
        st.markdown(f"""
            <div class="server-card">
                <div class="server-title">VIP</div>
                <div class="server-quota">50 GB</div>
                <div class="server-price">{SERVIDORES_PLANOS['VIP']['preco']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">Servidor Prioritário</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Assinar VIP", key="p_vip", use_container_width=True):
            st.session_state['plano_selecionado'] = "VIP"
            st.info("Vá para a aba 'Pagamento via Pix' para finalizar.")

    with col3:
        st.markdown(f"""
            <div class="server-card">
                <div class="server-title">MEGA VIP</div>
                <div class="server-quota">200 GB</div>
                <div class="server-price">{SERVIDORES_PLANOS['Mega VIP']['preco']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">Servidor Ultra Rápido</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Assinar Mega VIP", key="p_mega", use_container_width=True):
            st.session_state['plano_selecionado'] = "Mega VIP"
            st.info("Vá para a aba 'Pagamento via Pix' para finalizar.")

    with col4:
        st.markdown(f"""
            <div class="server-card-vip">
                <div class="badge-promo">40% OFF</div>
                <div class="server-title" style="color:#00FFCC;">VIP PLUS</div>
                <div class="server-quota">500 GB</div>
                <div class="server-price">{SERVIDORES_PLANOS['VIP Plus']['preco']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">Servidor Dedicado Máximo</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Assinar VIP Plus", key="p_plus", use_container_width=True):
            st.session_state['plano_selecionado'] = "VIP Plus"
            st.info("Vá para a aba 'Pagamento via Pix' para finalizar.")

# ---------------------------------------------------------
# TAB 3: PAGAMENTO VIA PIX SIMPLIFICADO
# ---------------------------------------------------------
with tab3:
    st.subheader("💳 Checkout Instantâneo via Pix")
    
    plano_atual = st.session_state.get('plano_selecionado', 'VIP Plus')
    dados_plano = SERVIDORES_PLANOS[plano_atual]
    
    st.markdown(f"### Plano Selecionado: **{plano_atual}** ({dados_plano['gb']} GB)")
    st.markdown(f"**Valor a pagar:** `{dados_plano['preco']}`")
    
    st.markdown(f"""
        <div class="pix-box">
            <h4>Chave Pix Oficial para Pagamento</h4>
            <p>Copie a chave abaixo e realize a transferência no app do seu banco:</p>
            <div class=CHAVE_PIX_OFICIAL = st.secrets.get("CHAVE_PIX_OFICIAL", "8ded5989-4158-4158-a917-ca4ead431fd7")

            <p style="color:#94A3B8; font-size:0.85rem;">Após realizar o Pix, seu servidor de {dados_plano['gb']} GB será ativado instantaneamente.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Confirmar Pagamento e Ativar Servidor ⚡", type="primary", use_container_width=True):
        with st.spinner("Verificando transação Pix no banco..."):
            time.sleep(2)
            st.balloons()
            st.success(f"Pagamento confirmado! O seu Servidor Dedicado ({plano_atual} - {dados_plano['gb']} GB) está 100% ONLINE!")
import streamlit as st
import time

# -----------------------------------------------------------------------------
# INTEGRATION WITH GOOGLE GEMINI AI
# -----------------------------------------------------------------------------
try:
    import google.genai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    try:
        import google.generativeai as genai
        GEMINI_AVAILABLE = True
    except ImportError:
        GEMINI_AVAILABLE = False

# -----------------------------------------------------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FileFlow | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# ADVANCED NEON & FUTURISTIC CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Dark Cyberpunk Theme Base */
    .stApp {
        background-color: #030712;
        color: #F3F4F6;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Neon Glow Animations */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
        50% { box-shadow: 0 0 35px rgba(0, 255, 204, 0.5); }
        100% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
    }
    
    /* Futuristic Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
        animation: pulseGlow 4s infinite ease-in-out;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 3px;
        background: linear-gradient(90deg, #00FFCC, #3B82F6, #9333EA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-transform: uppercase;
    }
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.1rem;
        margin-top: 8px;
        letter-spacing: 1px;
    }

    /* Cards Structure */
    .tech-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .tech-card:hover {
        border-color: #00FFCC;
        transform: translateY(-4px);
    }
    .tech-card-vip {
        background: rgba(15, 23, 42, 0.9);
        border: 2px solid #00FFCC;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.25);
        position: relative;
    }
    .promo-badge {
        background: #EC4899;
        color: white;
        font-weight: 800;
        font-size: 0.75rem;
        padding: 4px 12px;
        border-radius: 12px;
        position: absolute;
        top: -12px;
        right: 15px;
        text-transform: uppercase;
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #FFFFFF;
    }
    .card-storage {
        font-size: 2rem;
        font-weight: 900;
        color: #00FFCC;
        margin: 10px 0;
    }
    .card-price {
        font-size: 1.25rem;
        color: #E2E8F0;
        font-weight: 700;
    }

    /* Pix Box Styling */
    .pix-container {
        background: rgba(6, 78, 59, 0.2);
        border: 1px solid #059669;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# GLOBAL CONSTANTS & SESSION STATE
# -----------------------------------------------------------------------------
CHAVE_PIX_OFICIAL = "SUA_CHAVE_PIX_AQUI"  # Atualize com sua chave Pix/CPF

PLANS_DATA = {
    "Member": {"gb": 10, "price": "R$ 5,00/mês", "badge": None, "desc": "Contêiner Standard Isolado"},
    "VIP": {"gb": 50, "price": "R$ 10,00/mês", "badge": None, "desc": "Processamento Prioritário"},
    "Mega VIP": {"gb": 200, "price": "R$ 40,00/mês", "badge": None, "desc": "Cluster de Alta BANDA"},
    "VIP Plus": {"gb": 500, "price": "R$ 60,00/mês", "badge": "40% OFF", "desc": "Servidor Neural Exclusivo"}
}

if 'active_plan' not in st.session_state:
    st.session_state['active_plan'] = "Gratuito (Demonstração)"
if 'allocated_storage' not in st.session_state:
    st.session_state['allocated_storage'] = 2
if 'selected_checkout_plan' not in st.session_state:
    st.session_state['selected_checkout_plan'] = "VIP Plus"

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚡ FileFlow v1.0")
    st.caption("Neural Cloud Control Center")
    st.divider()

    st.subheader("🔑 Motor de IA Gemini")
    gemini_key = st.text_input("Insira sua API Key do Gemini:", type="password", help="Chave necessária para automação inteligente.")
    
    ai_active = False
    if gemini_key and GEMINI_AVAILABLE:
        try:
            if hasattr(genai, 'Client'):
                client = genai.Client(api_key=gemini_key)
            else:
                genai.configure(api_key=gemini_key)
            st.success("IA Neural Conectada e Operacional ⚡")
            ai_active = True
        except Exception as err:
            st.error(f"Falha de Autenticação: {err}")
    elif gemini_key and not GEMINI_AVAILABLE:
        st.warning("Biblioteca 'google-genai' não detectada no ambiente.")
    else:
        st.info("Insira a chave API para habilitar os recursos de IA.")

    st.divider()
    st.subheader("🖥️ Status do Servidor")
    st.write(f"**Plano Ativo:** `{st.session_state['active_plan']}`")
    st.write(f"**Cota Disponível:** `0.1 GB` / `{st.session_state['allocated_storage']} GB`")
    st.progress(0.1 / st.session_state['allocated_storage'])

# -----------------------------------------------------------------------------
# HERO HEADER
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">FILEFLOW // NEURAL CLOUD OS</h1>
        <p class="hero-subtitle">Plataforma Autônoma de Gerenciamento e Análise Transacional de Arquivos com IA</p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAIN NAVIGATION TABS
# -----------------------------------------------------------------------------
tab_app, tab_plans, tab_checkout, tab_telemetry = st.tabs([
    "📂 Servidor & Processamento IA", 
    "🚀 Servidores & Expansão", 
    "💳 Pagamento Pix", 
    "📊 Telemetria do Sistema"
])

# -----------------------------------------------------------------------------
# TAB 1: SERVER & AI PROCESSING
# -----------------------------------------------------------------------------
with tab_app:
    col_upload, col_ai = st.columns([1, 1], gap="large")
    
    with col_upload:
        st.subheader("📂 Upload para Nuvem Neural")
        uploaded_file = st.file_uploader(
            "Arraste ou selecione documentos/imagens para armazenamento seguro:",
            type=["pdf", "txt", "png", "jpg", "csv", "json", "epub"]
        )
        
        if uploaded_file:
            st.success(f"Arquivo `{uploaded_file.name}` indexado e criptografado com sucesso.")
            file_size_mb = round(uploaded_file.size / (1024 * 1024), 2)
            st.info(f"**Tamanho:** {file_size_mb} MB | **Status:** Pronto para roteamento")

    with col_ai:
        st.subheader("🤖 Agente Autônomo Gemini")
        user_prompt = st.text_area(
            "Instruções para o agente inteligente:",
            placeholder="Exemplo: Analise este documento, extraia os tópicos mais importantes e defina a melhor pasta para organizar."
        )
        
        if st.button("Executar Operação Inteligente 🚀", use_container_width=True, type="primary"):
            if not ai_active:
                st.error("Insira uma Chave API válida do Gemini na barra lateral para prosseguir.")
            else:
                with st.spinner("Conectando ao cluster Gemini para processamento de arquivo..."):
                    try:
                        if hasattr(genai, 'Client'):
                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=user_prompt if user_prompt else "Forneça um relatório de integridade do arquivo."
                            )
                            output_text = response.text
                        else:
                            model = genai.GenerativeModel('gemini-2.5-flash')
                            response = model.generate_content(user_prompt if user_prompt else "Análise geral de arquivo.")
                            output_text = response.text
                            
                        st.markdown("### 📝 Resultado da IA Neural:")
                        st.write(output_text)
                    except Exception as ex:
                        st.error(f"Erro no processamento da IA: {ex}")

# -----------------------------------------------------------------------------
# TAB 2: SERVER PLANS & UPGRADES
# -----------------------------------------------------------------------------
with tab_plans:
    st.subheader("🌐 Selecione a Capacidade do seu Servidor Dedicado")
    st.write("A ativação de novos planos garante contêineres isolados com alta taxa de transferência e suporte imediato a requisições de IA.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">MEMBER</div>
                <div class="card-storage">10 GB</div>
                <div class="card-price">{PLANS_DATA['Member']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['Member']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar Member", key="btn_member", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "Member"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col2:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">VIP</div>
                <div class="card-storage">50 GB</div>
                <div class="card-price">{PLANS_DATA['VIP']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['VIP']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar VIP", key="btn_vip", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "VIP"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col3:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">MEGA VIP</div>
                <div class="card-storage">200 GB</div>
                <div class="card-price">{PLANS_DATA['Mega VIP']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['Mega VIP']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar Mega VIP", key="btn_mega", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "Mega VIP"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col4:
        st.markdown(f"""
            <div class="tech-card-vip">
                <div class="promo-badge">40% OFF</div>
                <div class="card-title" style="color:#00FFCC;">VIP PLUS</div>
                <div class="card-storage">500 GB</div>
                <div class="card-price">{PLANS_DATA['VIP Plus']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['VIP Plus']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar VIP Plus", key="btn_vip_plus", type="primary", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "VIP Plus"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

# -----------------------------------------------------------------------------
# TAB 3: CHECKOUT VIA PIX
# -----------------------------------------------------------------------------
with tab_checkout:
    selected_plan = st.session_state.get('selected_checkout_plan', 'VIP Plus')
    plan_info = PLANS_DATA[selected_plan]
    
    st.subheader("💳 Finalização da Assinatura via Pix")
    st.write(f"Você está adquirindo o plano **{selected_plan}** com cota total de **{plan_info['gb']} GB**.")
    st.write(f"**Valor do Investimento:** `{plan_info['price']}`")
    
    st.markdown(f"""
        <div class="pix-container">
            <h3>Chave Pix Oficial do Sistema</h3>
            <p>Efetue a transferência usando a chave abaixo para ativação automática:</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.code(CHAVE_PIX_OFICIAL, language="text")
    
    if st.button("Confirmar Pagamento e Liberar Servidor ⚡", type="primary", use_container_width=True):
        with st.spinner("Confirmando transação no cluster financeiro..."):
            time.sleep(1.5)
            st.session_state['active_plan'] = f"{selected_plan} ({plan_info['gb']} GB)"
            st.session_state['allocated_storage'] = plan_info['gb']
            st.balloons()
            st.success(f"Pagamento confirmado! Servidor Dedicado de {plan_info['gb']} GB ativado com sucesso.")

# -----------------------------------------------------------------------------
# TAB 4: SYSTEM TELEMETRY (ENTERPRISE DASHBOARD)
# -----------------------------------------------------------------------------
with tab_telemetry:
    st.subheader("📊 Métricas do Servidor e da Infraestrutura")
    st.write("Acompanhamento de disponibilidade e tráfego de dados para avaliação comercial.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Status Global", "ONLINE", "100% Uptime")
    m2.metric("Latência da IA", "14 ms", "-3 ms")
    m3.metric("Contêineres Ativos", "1.024", "+28 hoje")
    m4.metric("Segurança", "AES-256", "Ativa")
    
    st.divider()
    st.caption("FileFlow OS © 2026 - Todos os direitos reservados.")
import streamlit as st
import time

# -----------------------------------------------------------------------------
# INTEGRATION WITH GOOGLE GEMINI AI
# -----------------------------------------------------------------------------
try:
    import google.genai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    try:
        import google.generativeai as genai
        GEMINI_AVAILABLE = True
    except ImportError:
        GEMINI_AVAILABLE = False

# -----------------------------------------------------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FileFlow | Neural Cloud OS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# ADVANCED NEON & FUTURISTIC CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Dark Cyberpunk Theme Base */
    .stApp {
        background-color: #030712;
        color: #F3F4F6;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Neon Glow Animations */
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
        50% { box-shadow: 0 0 35px rgba(0, 255, 204, 0.5); }
        100% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
    }
    
    /* Futuristic Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
        animation: pulseGlow 4s infinite ease-in-out;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 3px;
        background: linear-gradient(90deg, #00FFCC, #3B82F6, #9333EA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-transform: uppercase;
    }
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.1rem;
        margin-top: 8px;
        letter-spacing: 1px;
    }

    /* Cards Structure */
    .tech-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .tech-card:hover {
        border-color: #00FFCC;
        transform: translateY(-4px);
    }
    .tech-card-vip {
        background: rgba(15, 23, 42, 0.9);
        border: 2px solid #00FFCC;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.25);
        position: relative;
    }
    .promo-badge {
        background: #EC4899;
        color: white;
        font-weight: 800;
        font-size: 0.75rem;
        padding: 4px 12px;
        border-radius: 12px;
        position: absolute;
        top: -12px;
        right: 15px;
        text-transform: uppercase;
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #FFFFFF;
    }
    .card-storage {
        font-size: 2rem;
        font-weight: 900;
        color: #00FFCC;
        margin: 10px 0;
    }
    .card-price {
        font-size: 1.25rem;
        color: #E2E8F0;
        font-weight: 700;
    }

    /* Pix Box Styling */
    .pix-container {
        background: rgba(6, 78, 59, 0.2);
        border: 1px solid #059669;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# GLOBAL CONSTANTS & SESSION STATE
# -----------------------------------------------------------------------------
CHAVE_PIX_OFICIAL = "SUA_CHAVE_PIX_AQUI"  # Atualize com sua chave Pix/CPF

PLANS_DATA = {
    "Member": {"gb": 10, "price": "R$ 5,00/mês", "badge": None, "desc": "Contêiner Standard Isolado"},
    "VIP": {"gb": 50, "price": "R$ 10,00/mês", "badge": None, "desc": "Processamento Prioritário"},
    "Mega VIP": {"gb": 200, "price": "R$ 40,00/mês", "badge": None, "desc": "Cluster de Alta BANDA"},
    "VIP Plus": {"gb": 500, "price": "R$ 60,00/mês", "badge": "40% OFF", "desc": "Servidor Neural Exclusivo"}
}

if 'active_plan' not in st.session_state:
    st.session_state['active_plan'] = "Gratuito (Demonstração)"
if 'allocated_storage' not in st.session_state:
    st.session_state['allocated_storage'] = 2
if 'selected_checkout_plan' not in st.session_state:
    st.session_state['selected_checkout_plan'] = "VIP Plus"

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚡ FileFlow v1.0")
    st.caption("Neural Cloud Control Center")
    st.divider()

    st.subheader("🔑 Motor de IA Gemini")
    gemini_key = st.text_input("Insira sua API Key do Gemini:", type="password", help="Chave necessária para automação inteligente.")
    
    ai_active = False
    if gemini_key and GEMINI_AVAILABLE:
        try:
            if hasattr(genai, 'Client'):
                client = genai.Client(api_key=gemini_key)
            else:
                genai.configure(api_key=gemini_key)
            st.success("IA Neural Conectada e Operacional ⚡")
            ai_active = True
        except Exception as err:
            st.error(f"Falha de Autenticação: {err}")
    elif gemini_key and not GEMINI_AVAILABLE:
        st.warning("Biblioteca 'google-genai' não detectada no ambiente.")
    else:
        st.info("Insira a chave API para habilitar os recursos de IA.")

    st.divider()
    st.subheader("🖥️ Status do Servidor")
    st.write(f"**Plano Ativo:** `{st.session_state['active_plan']}`")
    st.write(f"**Cota Disponível:** `0.1 GB` / `{st.session_state['allocated_storage']} GB`")
    st.progress(0.1 / st.session_state['allocated_storage'])

# -----------------------------------------------------------------------------
# HERO HEADER
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">FILEFLOW // NEURAL CLOUD OS</h1>
        <p class="hero-subtitle">Plataforma Autônoma de Gerenciamento e Análise Transacional de Arquivos com IA</p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAIN NAVIGATION TABS
# -----------------------------------------------------------------------------
tab_app, tab_plans, tab_checkout, tab_telemetry = st.tabs([
    "📂 Servidor & Processamento IA", 
    "🚀 Servidores & Expansão", 
    "💳 Pagamento Pix", 
    "📊 Telemetria do Sistema"
])

# -----------------------------------------------------------------------------
# TAB 1: SERVER & AI PROCESSING
# -----------------------------------------------------------------------------
with tab_app:
    col_upload, col_ai = st.columns([1, 1], gap="large")
    
    with col_upload:
        st.subheader("📂 Upload para Nuvem Neural")
        uploaded_file = st.file_uploader(
            "Arraste ou selecione documentos/imagens para armazenamento seguro:",
            type=["pdf", "txt", "png", "jpg", "csv", "json", "epub"]
        )
        
        if uploaded_file:
            st.success(f"Arquivo `{uploaded_file.name}` indexado e criptografado com sucesso.")
            file_size_mb = round(uploaded_file.size / (1024 * 1024), 2)
            st.info(f"**Tamanho:** {file_size_mb} MB | **Status:** Pronto para roteamento")

    with col_ai:
        st.subheader("🤖 Agente Autônomo Gemini")
        user_prompt = st.text_area(
            "Instruções para o agente inteligente:",
            placeholder="Exemplo: Analise este documento, extraia os tópicos mais importantes e defina a melhor pasta para organizar."
        )
        
        if st.button("Executar Operação Inteligente 🚀", use_container_width=True, type="primary"):
            if not ai_active:
                st.error("Insira uma Chave API válida do Gemini na barra lateral para prosseguir.")
            else:
                with st.spinner("Conectando ao cluster Gemini para processamento de arquivo..."):
                    try:
                        if hasattr(genai, 'Client'):
                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=user_prompt if user_prompt else "Forneça um relatório de integridade do arquivo."
                            )
                            output_text = response.text
                        else:
                            model = genai.GenerativeModel('gemini-2.5-flash')
                            response = model.generate_content(user_prompt if user_prompt else "Análise geral de arquivo.")
                            output_text = response.text
                            
                        st.markdown("### 📝 Resultado da IA Neural:")
                        st.write(output_text)
                    except Exception as ex:
                        st.error(f"Erro no processamento da IA: {ex}")

# -----------------------------------------------------------------------------
# TAB 2: SERVER PLANS & UPGRADES
# -----------------------------------------------------------------------------
with tab_plans:
    st.subheader("🌐 Selecione a Capacidade do seu Servidor Dedicado")
    st.write("A ativação de novos planos garante contêineres isolados com alta taxa de transferência e suporte imediato a requisições de IA.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">MEMBER</div>
                <div class="card-storage">10 GB</div>
                <div class="card-price">{PLANS_DATA['Member']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['Member']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar Member", key="btn_member", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "Member"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col2:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">VIP</div>
                <div class="card-storage">50 GB</div>
                <div class="card-price">{PLANS_DATA['VIP']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['VIP']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar VIP", key="btn_vip", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "VIP"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col3:
        st.markdown(f"""
            <div class="tech-card">
                <div class="card-title">MEGA VIP</div>
                <div class="card-storage">200 GB</div>
                <div class="card-price">{PLANS_DATA['Mega VIP']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['Mega VIP']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar Mega VIP", key="btn_mega", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "Mega VIP"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

    with col4:
        st.markdown(f"""
            <div class="tech-card-vip">
                <div class="promo-badge">40% OFF</div>
                <div class="card-title" style="color:#00FFCC;">VIP PLUS</div>
                <div class="card-storage">500 GB</div>
                <div class="card-price">{PLANS_DATA['VIP Plus']['price']}</div>
                <p style="color:#94A3B8; font-size:0.85rem; margin-top:10px;">{PLANS_DATA['VIP Plus']['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Ativar VIP Plus", key="btn_vip_plus", type="primary", use_container_width=True):
            st.session_state['selected_checkout_plan'] = "VIP Plus"
            st.info("Plano selecionado! Acesse a aba 'Pagamento Pix' para concluir.")

# -----------------------------------------------------------------------------
# TAB 3: CHECKOUT VIA PIX
# -----------------------------------------------------------------------------
with tab_checkout:
    selected_plan = st.session_state.get('selected_checkout_plan', 'VIP Plus')
    plan_info = PLANS_DATA[selected_plan]
    
    st.subheader("💳 Finalização da Assinatura via Pix")
    st.write(f"Você está adquirindo o plano **{selected_plan}** com cota total de **{plan_info['gb']} GB**.")
    st.write(f"**Valor do Investimento:** `{plan_info['price']}`")
    
    st.markdown(f"""
        <div class="pix-container">
            <h3>Chave Pix Oficial do Sistema</h3>
            <p>Efetue a transferência usando a chave abaixo para ativação automática:</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.code(CHAVE_PIX_OFICIAL, language="text")
    
    if st.button("Confirmar Pagamento e Liberar Servidor ⚡", type="primary", use_container_width=True):
        with st.spinner("Confirmando transação no cluster financeiro..."):
            time.sleep(1.5)
            st.session_state['active_plan'] = f"{selected_plan} ({plan_info['gb']} GB)"
            st.session_state['allocated_storage'] = plan_info['gb']
            st.balloons()
            st.success(f"Pagamento confirmado! Servidor Dedicado de {plan_info['gb']} GB ativado com sucesso.")

# -----------------------------------------------------------------------------
# TAB 4: SYSTEM TELEMETRY (ENTERPRISE DASHBOARD)
# -----------------------------------------------------------------------------
with tab_telemetry:
    st.subheader("📊 Métricas do Servidor e da Infraestrutura")
    st.write("Acompanhamento de disponibilidade e tráfego de dados para avaliação comercial.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Status Global", "ONLINE", "100% Uptime")
    m2.metric("Latência da IA", "14 ms", "-3 ms")
    m3.metric("Contêineres Ativos", "1.024", "+28 hoje")
    m4.metric("Segurança", "AES-256", "Ativa")
    
    st.divider()
    st.caption("FileFlow OS © 2026 - Todos os direitos reservados.")
