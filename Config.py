import streamlit as st

# CHAVE PIX FIXA E DADOS DOS PLANOS
CHAVE_PIX_OFICIAL = "8ded9989-4158-4171-a917-ca6ea4d31fd7"

PLANS_DATA = {
    "Member": {
        "gb": 10,
        "price": "R$ 5,00/mês",
        "badge": "None",
        "desc": "Container Estandard Isolado",
    },
    "VIP": {
        "gb": 50,
        "price": "R$ 10,00/mês",
        "badge": "Novo",
        "desc": "Processamento Prioritário",
    },
    "Mega VIP": {
        "gb": 200,
        "price": "R$ 40,00/mês",
        "badge": "None",
        "desc": "Cluster de Alta Banda",
    },
    "VIP Plus": {
        "gb": 500,
        "price": "R$ 60,00/mês",
        "badge": "Desconto 40%",
        "desc": "Servidor Neural Exclusivo",
    },
}
