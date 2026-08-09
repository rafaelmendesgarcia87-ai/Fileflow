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
