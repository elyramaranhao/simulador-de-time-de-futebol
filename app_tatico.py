import streamlit as st
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Simulador Tático", layout="wide")

# Dados de formações (posição no campo: x, y)
formacoes = {
    "4-3-3": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 8, 20),
        ("LE", 0, 30), ("LD", 10, 30),
        ("VOL", 5, 40),
        ("MC", 3, 50), ("MC", 7, 50),
        ("PE", 1, 70), ("PD", 9, 70), ("ATA", 5, 80)
    ],
    "4-2-3-1": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 8, 20),
        ("LE", 0, 30), ("LD", 10, 30),
        ("VOL", 3, 40), ("VOL", 7, 40),
        ("MEI", 3, 55), ("MEI", 5, 60), ("MEI", 7, 55),
        ("ATA", 5, 75)
    ],
    "3-5-2": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 5, 20), ("ZAG", 8, 20),
        ("ALA", 0, 40), ("ALA", 10, 40),
        ("VOL", 4, 40), ("VOL", 6, 40),
        ("MC", 3, 55), ("MC", 7, 55),
        ("ATA", 4, 75), ("ATA", 6, 75)
    ]
}

# Sessão para armazenar estado
if "page" not in st.session_state:
    st.session_state.page = "formacao"
if "formacao" not in st.session_state:
    st.session_state.formacao = "4-3-3"
if "jogadores" not in st.session_state:
    st.session_state.jogadores = {}

# Navegação entre páginas
def mudar_pagina(nova):
    st.session_state.page = nova

# Página 1 – Escolher Formação
if st.session_state.page == "formacao":
    st.title("📐 Escolha a Formação Tática")
    formacao = st.selectbox("Escolha o esquema tático:", list(formacoes.keys()))
    if st.button("Avançar"):
        st.session_state.formacao = formacao
        st.session_state.jogadores = {}
        mudar_pagina("jogadores")

# Página 2 – Montar Time
elif st.session_state.page == "jogadores":
    st.title("✏️ Monte seu Time")
    posicoes = formacoes[st.session_state.formacao]
    with st.form("form_jogadores"):
        for i, (pos, x, y) in enumerate(posicoes):
            nome = st.text_input(f"{pos} ({i+1})", key=f"jogador_{i}")
            st.session_state.jogadores[i] = nome
        if st.form_submit_button("Visualizar Esquema"):
            mudar_pagina("analise")

# Página 3 – Visualização e Análise
elif st.session_state.page == "analise":
    st.title("📊 Esquema em Campo + Análise")

    posicoes = formacoes[st.session_state.formacao]
    jogadores = st.session_state.jogadores

    # Desenha campo
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_facecolor("#4CAF50")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)
    ax.axis("off")

    for i, (pos, x, y) in enumerate(posicoes):
        nome = jogadores.get(i, "")
        ax.add_patch(plt.Circle((x, y), 1, color="white"))
        ax.text(x, y, nome[:3].upper(), ha="center", va="center", fontsize=8, weight="bold")

    st.pyplot(fig, use_container_width=True)

    # Indicadores táticos simples
    total = len(posicoes)
    atacantes = sum(1 for pos, _, _ in posicoes if pos in ["ATA", "PD", "PE"])
    meio = sum(1 for pos, _, _ in posicoes if pos in ["MC", "MEI", "VOL"])
    defesa = sum(1 for pos, _, _ in posicoes if pos in ["ZAG", "LE", "LD"])

    st.markdown("### 🧠 Indicadores Táticos")
    st.metric("Agressividade", f"{round(100 * atacantes / total)}%")
    st.metric("Controle de Jogo", f"{round(100 * meio / total)}%")
    st.metric("Cobertura Defensiva", f"{round(100 * defesa / total)}%")

    if st.button("Voltar"):
        mudar_pagina("formacao")
