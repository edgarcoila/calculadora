import streamlit as st
from math import sqrt, log

st.set_page_config(page_title="Artritis Reumatoide", layout="centered")
st.title("Artritis Reumatoide")

def das28_esr(tjc28, sjc28, vsr, gh):
    vsr = vsr if vsr >= 1 else 1
    return round(0.56 * sqrt(tjc28) + 0.28 * sqrt(sjc28) + 0.70 * log(vsr) + 0.014 * gh, 2)

def das28_crp(tjc28, sjc28, crp, gh):
    return round(0.56 * sqrt(tjc28) + 0.28 * sqrt(sjc28) + 0.36 * log(crp + 1) + 0.014 * gh + 0.96, 2)

def cdai(tjc28, sjc28, pga, ega):
    return round(tjc28 + sjc28 + pga + ega, 2)

def sdai(tjc28, sjc28, pga, ega, crp):
    return round(tjc28 + sjc28 + pga + ega + crp, 2)

st.subheader("DAS28 – VSG")
with st.form("form_das28_vsg"):
    tjc = st.number_input("TJC28", min_value=0, value=0)
    sjc = st.number_input("SJC28", min_value=0, value=0)
    vsr = st.number_input("VSG (mm/h)", min_value=0.0, value=0.0)
    gh = st.number_input("GH (0–100)", min_value=0.0, value=0.0)
    if st.form_submit_button("Calcular"):
        resultado = das28_esr(tjc, sjc, vsr, gh)
        st.success(f"DAS28-VSG: {resultado}")

st.subheader("DAS28 – PCR")
with st.form("form_das28_pcr"):
    tjc = st.number_input("TJC28", min_value=0, value=0, key="d2_tjc")
    sjc = st.number_input("SJC28", min_value=0, value=0, key="d2_sjc")
    crp = st.number_input("PCR (mg/L)", min_value=0.0, value=0.0, key="d2_crp")
    gh = st.number_input("GH (0–100)", min_value=0.0, value=0.0, key="d2_gh")
    if st.form_submit_button("Calcular"):
        resultado = das28_crp(tjc, sjc, crp, gh)
        st.success(f"DAS28-PCR: {resultado}")

st.subheader("CDAI")
with st.form("form_cdai"):
    tjc = st.number_input("TJC28", min_value=0, value=0, key="c_tjc")
    sjc = st.number_input("SJC28", min_value=0, value=0, key="c_sjc")
    pga = st.number_input("PGA (0–10)", min_value=0.0, value=0.0, key="c_pga")
    ega = st.number_input("EGA (0–10)", min_value=0.0, value=0.0, key="c_ega")
    if st.form_submit_button("Calcular"):
        resultado = cdai(tjc, sjc, pga, ega)
        st.success(f"CDAI: {resultado}")

st.subheader("SDAI")
with st.form("form_sdai"):
    tjc = st.number_input("TJC28", min_value=0, value=0, key="s_tjc")
    sjc = st.number_input("SJC28", min_value=0, value=0, key="s_sjc")
    pga = st.number_input("PGA (0–10)", min_value=0.0, value=0.0, key="s_pga")
    ega = st.number_input("EGA (0–10)", min_value=0.0, value=0.0, key="s_ega")
    crp = st.number_input("PCR (mg/dL)", min_value=0.0, value=0.0, key="s_crp")
    if st.form_submit_button("Calcular"):
        resultado = sdai(tjc, sjc, pga, ega, crp)
        st.success(f"SDAI: {resultado}")