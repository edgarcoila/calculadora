import streamlit as st

st.set_page_config(page_title="Calculadora de Actividad Reumatológica", layout="centered")

from pages import Artritis_reumatoide, Lupus_eritematoso

st.title("🧮 Calculadora de Actividad Reumatológica")

st.write("Seleccione una opción:")

if st.button("Artritis Reumatoide"):
    st.switch_page("pages/Artritis_reumatoide.py")

if st.button("Lupus Eritematoso Sistémico"):
    st.switch_page("pages/Lupus_eritematoso.py")
