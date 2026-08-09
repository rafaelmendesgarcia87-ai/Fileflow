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
