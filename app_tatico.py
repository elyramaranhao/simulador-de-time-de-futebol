import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Simulador Tático", layout="wide")
st.title("⚽ Simulador Tático de Futebol")

# --- Formações disponíveis ---
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
        ("VOL", 4, 45), ("VOL", 6, 45),
        ("MC", 5, 55),
        ("ATA", 4, 75), ("ATA", 6, 75)
    ],
    "4-4-2": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 8, 20),
        ("LE", 0, 30), ("LD", 10, 30),
        ("MC", 2, 45), ("MC", 8, 45),
        ("ME", 0, 55), ("MD", 10, 55),
        ("ATA", 4, 75), ("ATA", 6, 75)
    ],
    "3-4-3": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 5, 20), ("ZAG", 8, 20),
        ("ALA", 1, 40), ("ALA", 9, 40),
        ("MC", 3, 50), ("MC", 7, 50),
        ("PE", 2, 70), ("PD", 8, 70), ("ATA", 5, 75)
    ],
    "4-1-4-1": [
        ("GOL", 5, 5),
        ("ZAG", 2, 20), ("ZAG", 8, 20),
        ("LE", 0, 30), ("LD", 10, 30),
        ("VOL", 5, 40),
        ("ME", 2, 50), ("MC", 4, 50), ("MC", 6, 50), ("MD", 8, 50),
        ("ATA", 5, 75)
    ]
}

# Estilos de adversário
estilos_adversario = {
    "Time Reativo": "Ataca em transição rápida, defesa baixa, cede posse.",
    "Pressão Alta": "Marcação adiantada, obriga saída rápida e precisa.",
    "Posse de Bola": "Controla jogo no meio, atrai marcação e busca infiltrações.",
    "Bloqueio Central": "Congestiona o meio, força jogadas pelas laterais.",
    "Linha Alta": "Joga com zaga avançada, explora impedimento."
}
