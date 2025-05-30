# Esta pendiente agregar el logo
# Personalizar un poco más

import streamlit as st

st.set_page_config(page_title="Clinimetría", layout="centered")

from pages import artritis_reumatoide, lupus_eritematoso

st.title("🧮 Clinimetría")

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://reumatoperu.org" target="_blank" style="font-size:2rem; font-weight:bold; color:#3366cc; text-decoration:none;">
            reumatoperu.org
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


st.write("Seleccione una opción:")

if st.button("Artritis Reumatoide"):
    st.switch_page("pages/artritis_reumatoide.py")

if st.button("Lupus Eritematoso Sistémico"):
    st.switch_page("pages/lupus_eritematoso.py")
