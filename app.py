import streamlit as st
import math

# --- Funciones de cálculo ---
def das28_esr(tjc28, sjc28, vsr, gh):
    vsr = vsr if vsr >= 1 else 1
    return round(0.56 * math.sqrt(tjc28) + 0.28 * math.sqrt(sjc28) + 0.70 * math.log(vsr) + 0.014 * gh, 2)

def das28_crp(tjc28, sjc28, crp, gh):
    return round(0.56 * math.sqrt(tjc28) + 0.28 * math.sqrt(sjc28) + 0.36 * math.log(crp + 1) + 0.014 * gh + 0.96, 2)

def cdai(tjc28, sjc28, pga, ega):
    return round(tjc28 + sjc28 + pga + ega, 2)

def sdai(tjc28, sjc28, pga, ega, crp):
    return round(tjc28 + sjc28 + pga + ega + crp, 2)

sle2_weights = {
    'convulsiones': 8, 'psicosis': 8, 'cerebral': 8,
    'vision': 8, 'neuropatia': 8, 'vasculitis': 8,
    'cefalea': 8, 'acv': 8,
    'artritis': 4, 'miositis': 4,
    'hematuria': 4, 'proteinuria': 4, 'cilindros': 4, 'piuria': 4,
    'rash': 2, 'alopecia': 2, 'ulceras_orales': 2,
    'pleuritis': 2, 'pericarditis': 2,
    'fiebre': 2, 'trombocitopenia': 2, 'leucopenia': 2,
    'complemento_bajo': 2, 'antiDNA': 2
}

def sledai_2k(present_items):
    return sum(sle2_weights[item] for item in present_items if item in sle2_weights)

def interpret_sledai(score):
    if score == 0:
        return "Inactivo"
    elif 1 <= score <= 5:
        return "Actividad leve"
    elif 6 <= score <= 10:
        return "Actividad moderada"
    else:
        return "Alta actividad"

# --- Interfaz Streamlit ---
st.title("Calculadora de Actividad Reumatológica")
st.subheader("Artritis Reumatoide")

tjc28 = st.slider("TJC28 - Articulaciones dolorosas", 0, 28, 6)
sjc28 = st.slider("SJC28 - Articulaciones inflamadas", 0, 28, 4)
vsr = st.number_input("VSG (mm/h)", min_value=0.0, value=25.0)
crp = st.number_input("PCR (mg/L)", min_value=0.0, value=8.2)
gh = st.slider("GH - Evaluación del paciente (0-100 mm)", 0, 100, 60)
pga = st.slider("PGA - Evaluación global del paciente (0–10)", 0.0, 10.0, 5.0)
ega = st.slider("EGA - Evaluación global del médico (0–10)", 0.0, 10.0, 4.0)

st.markdown("---")
st.subheader("Lupus Eritematoso Sistémico - SLEDAI-2K")
selected_items = st.multiselect("Selecciona los ítems presentes", options=list(sle2_weights.keys()))

# --- Cálculo de resultados ---
if st.button("Calcular Scores"):
    sle_score = sledai_2k(selected_items)
    results = {
        "DAS28–VSG": das28_esr(tjc28, sjc28, vsr, gh),
        "DAS28–PCR": das28_crp(tjc28, sjc28, crp, gh),
        "CDAI": cdai(tjc28, sjc28, pga, ega),
        "SDAI": sdai(tjc28, sjc28, pga, ega, crp),
        "SLEDAI-2K": sle_score
    }
    
    st.markdown("### Resultados")
    for k, v in results.items():
        st.write(f"**{k}**: {v}")

    st.write(f"**Interpretación SLEDAI-2K**: {interpret_sledai(sle_score)}")
