import streamlit as st

st.set_page_config(page_title="Lupus Eritematoso Sistémico", layout="centered")
st.title("Lupus Eritematoso Sistémico")

sle2_weights = {
    'Convulsiones':8, 'Psicosis':8, 'Síndrome orgánico cerebral':8,
    'Pérdida de visión':8, 'Neuropatía craneal':8, 'Vasculitis sistémica':8,
    'Cefalea lúpica':8, 'ACV':8,
    'Artritis':4, 'Miositis':4,
    'Hematuria':4, 'Proteinuria':4, 'Cilindros urinarios':4, 'Piuria':4,
    'Erupción cutánea':2, 'Alopecia':2, 'Úlceras orales':2,
    'Pleuritis':2, 'Pericarditis':2,
    'Fiebre':2, 'Trombocitopenia':2, 'Leucopenia':2,
    'Complemento bajo':2, 'Anti-DNA elevado':2
}

st.subheader("Ítems clínicos presentes")
selected = st.multiselect("Seleccione los ítems presentes en los últimos 10 días:", options=sle2_weights.keys())

def interpretacion(score):
    if score == 0:
        return "Inactividad"
    elif score <= 5:
        return "Actividad leve"
    elif score <= 10:
        return "Actividad moderada"
    else:
        return "Alta actividad"

if st.button("Calcular"):
    total = sum(sle2_weights[item] for item in selected)
    st.success(f"SLEDAI-2K: {total} — {interpretacion(total)}")