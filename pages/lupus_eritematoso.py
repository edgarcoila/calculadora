import streamlit as st

st.title("🧬 Lupus Eritematoso Sistémico - SLEDAI-2K")

st.write("Seleccione los ítems presentes en los últimos 10 días. Cada ítem tiene un peso específico según la gravedad clínica.")

items = {
    'Convulsiones': (8, 'Episodios súbitos de actividad eléctrica cerebral anormal, con pérdida de conciencia o movimientos involuntarios.'),
    'Psicosis': (8, 'Trastorno mental grave que implica una desconexión con la realidad, incluyendo alucinaciones o delirios.'),
    'Síndrome orgánico cerebral': (8, 'Disfunción cerebral con síntomas cognitivos, de conciencia o comportamiento.'),
    'Pérdida de visión': (8, 'Disminución súbita o progresiva de la visión no atribuible a causas mecánicas.'),
    'Neuropatía craneal': (8, 'Alteración de los nervios craneales, con parálisis facial o pérdida sensorial.'),
    'Vasculitis sistémica': (8, 'Inflamación de vasos sanguíneos en múltiples órganos.'),
    'Cefalea lúpica': (8, 'Dolor de cabeza intenso, persistente y no explicado por otra causa.'),
    'ACV': (8, 'Accidente cerebrovascular isquémico o hemorrágico evidenciado clínicamente.'),
    'Artritis': (4, 'Inflamación en dos o más articulaciones con dolor, hinchazón o movimiento limitado.'),
    'Miositis': (4, 'Inflamación de los músculos con debilidad proximal o dolor.'),
    'Hematuria': (4, 'Presencia de sangre en la orina.'),
    'Proteinuria': (4, 'Excreción anormal de proteínas en la orina.'),
    'Cilindros urinarios': (4, 'Formaciones proteicas en el sedimento urinario observadas al microscopio.'),
    'Piuria': (4, 'Presencia de pus o leucocitos en la orina.'),
    'Erupción cutánea': (2, 'Lesiones cutáneas típicas del lupus, como el rash malar.'),
    'Alopecia': (2, 'Pérdida anormal de cabello.'),
    'Úlceras orales': (2, 'Lesiones dolorosas en la mucosa oral o nasal.'),
    'Pleuritis': (2, 'Dolor torácico pleurítico con roce o derrame.'),
    'Pericarditis': (2, 'Inflamación del pericardio con o sin derrame.'),
    'Fiebre': (2, 'Temperatura mayor a 38°C sin causa infecciosa evidente.'),
    'Trombocitopenia': (2, 'Conteo de plaquetas menor de 100,000/mm³ sin otra causa.'),
    'Leucopenia': (2, 'Conteo de leucocitos menor de 3,000/mm³.'),
    'Complemento bajo': (2, 'Disminución de C3, C4 o CH50.'),
    'Anti-DNA elevado': (2, 'Títulos elevados de anticuerpos anti-DNA en suero.')
}

total = 0
for label, (peso, descripcion) in items.items():
    col1, col2 = st.columns([1, 4])
    with col1:
        checked = st.checkbox(f"{label} ({peso})", key=label)
    with col2:
        st.markdown(f"<small>{descripcion}</small>", unsafe_allow_html=True)
    if checked:
        total += peso

if st.button("Calcular SLEDAI-2K"):
    st.success(f"SLEDAI-2K: {total}")

    if total == 0:
        st.info("Interpretación: Inactivo")
    elif total <= 5:
        st.info("Interpretación: Actividad leve")
    elif total <= 10:
        st.warning("Interpretación: Actividad moderada")
    else:
        st.error("Interpretación: Alta actividad")