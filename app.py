import streamlit as st
from pages import artritis_reumatoide, lupus

st.set_page_config(page_title="Calculadora Reumatológica", layout="centered")

st.title("Calculadora de Actividad Reumatológica")

st.write("Seleccione una condición para evaluar:")

col1, col2 = st.columns(2)
with col1:
    if st.button("Artritis Reumatoide"):
        st.switch_page("pages/artritis_reumatoide.py")
with col2:
    if st.button("Lupus Eritematoso Sistémico"):
        st.switch_page("pages/lupus.py")