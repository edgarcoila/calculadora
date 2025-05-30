
import streamlit as st
import math

st.title("🦴 Artritis Reumatoide")

# Componentes compartidos
tjc28 = st.number_input("TJC28 - Articulaciones dolorosas (0–28)", min_value=0, step=1)
sjc28 = st.number_input("SJC28 - Articulaciones inflamadas (0–28)", min_value=0, step=1)
gh = st.number_input("GH - Evaluación global de salud (0–100 mm)", min_value=0.0, max_value=100.0)

# DAS28-VSG
st.header("🔹 DAS28–VSG")
vsr = st.number_input("VSG - Velocidad de sedimentación globular (mm/h)", min_value=0.0)
if st.button("Calcular DAS28–VSG"):
    if any(v is None or v == '' for v in [tjc28, sjc28, vsr, gh]):
        st.error("Todos los campos deben ser completados.")
    else:
        vsr = vsr if vsr >= 1 else 1
        das28_vsg = 0.56 * math.sqrt(tjc28) + 0.28 * math.sqrt(sjc28) + 0.70 * math.log(vsr) + 0.014 * gh
        st.success(f"DAS28–VSG: {das28_vsg:.2f}")

# DAS28-PCR
st.header("🔹 DAS28–PCR")
crp = st.number_input("PCR - Proteína C reactiva (mg/L)", min_value=0.0)
if st.button("Calcular DAS28–PCR"):
    if any(v is None or v == '' for v in [tjc28, sjc28, crp, gh]):
        st.error("Todos los campos deben ser completados.")
    else:
        das28_pcr = 0.56 * math.sqrt(tjc28) + 0.28 * math.sqrt(sjc28) + 0.36 * math.log(crp + 1) + 0.014 * gh + 0.96
        st.success(f"DAS28–PCR: {das28_pcr:.2f}")

# CDAI
st.header("🔹 CDAI")
pga = st.number_input("PGA - Autoevaluación del paciente (0–10)", min_value=0.0, max_value=10.0)
ega = st.number_input("EGA - Evaluación del médico (0–10)", min_value=0.0, max_value=10.0)
if st.button("Calcular CDAI"):
    if any(v is None or v == '' for v in [tjc28, sjc28, pga, ega]):
        st.error("Todos los campos deben ser completados.")
    else:
        cdai = tjc28 + sjc28 + pga + ega
        st.success(f"CDAI: {cdai:.2f}")

# SDAI
st.header("🔹 SDAI")
crp_sdai = st.number_input("PCR (mg/dL) para SDAI", min_value=0.0)
if st.button("Calcular SDAI"):
    if any(v is None or v == '' for v in [tjc28, sjc28, pga, ega, crp_sdai]):
        st.error("Todos los campos deben ser completados.")
    else:
        sdai = tjc28 + sjc28 + pga + ega + crp_sdai
        st.success(f"SDAI: {sdai:.2f}")