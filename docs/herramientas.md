A continuación encontrarás el detalle de cada escala, con la definición de sus componentes y la fórmula exacta para que puedas implementarlas en tu aplicación.

---

## ARTRITIS REUMATOIDE

### 1. DAS28–VSG

*Componentes*

* TJC28: Número de articulaciones dolorosas (28 articulaciones)
* SJC28: Número de articulaciones inflamadas (28 articulaciones)
* VSG: Velocidad de sedimentación globular (mm/h)
* GH: Evaluación global de salud por el/la paciente (0–100 mm en escala visual análoga)

*Fórmula* (Prevoo et al. 1995)

$$
\text{DAS28–VSG} = 0{,}56 \times \sqrt{\text{TJC28}} \;+\; 0{,}28 \times \sqrt{\text{SJC28}} \;+\; 0{,}70 \times \ln(\text{VSG}) \;+\; 0{,}014 \times \text{GH}
$$

> *Nota*: si VSG = 0 usar VSG = 1 para el término logarítmico.

---

### 2. DAS28–PCR

*Componentes*

* TJC28, SJC28, GH: como en DAS28–VSG
* PCR: Proteína C reactiva en mg/L

*Fórmula* (Inoue et al. 2007)

$$
\text{DAS28–PCR} = 0{,}56 \times \sqrt{\text{TJC28}} \;+\; 0{,}28 \times \sqrt{\text{SJC28}} \;+\; 0{,}36 \times \ln(\text{PCR} + 1) \;+\; 0{,}014 \times \text{GH} \;+\; 0{,}96
$$

> *Nota*: la constante +1 dentro del logaritmo evita problemas si PCR = 0.

---

### 3. CDAI (Clinical Disease Activity Index)

*Componentes*

* TJC28
* SJC28
* PGA: Patient Global Assessment (0–10)
* EGA: Evaluator (Physician) Global Assessment (0–10)

*Cálculo*

$$
\text{CDAI} = \text{TJC28} + \text{SJC28} + \text{PGA} + \text{EGA}
$$

---

### 4. SDAI (Simplified Disease Activity Index)

*Componentes*

* Todos los de la CDAI (TJC28, SJC28, PGA, EGA)
* PCR: Proteína C reactiva (mg/dL)

*Cálculo*

$$
\text{SDAI} = \text{TJC28} + \text{SJC28} + \text{PGA} + \text{EGA} + \text{PCR}
$$

---

## LUPUS ERITEMATOSO SISTÉMICO

### SLEDAI-2K (Systemic Lupus Erythematosus Disease Activity Index 2000)

Es un score de suma de ítems, cada uno con un peso fijo que refleja la gravedad de la manifestación en las últimas 10 días.

| Ítem clínico/lab.                                                                                                                            | Peso |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Convulsiones, Psicosis, Síndrome orgánico (cerebral)                                                                                         | 8    |
| Pérdida de visión, neuropatía craneal, vasculitis sistémica, Cefalea lúpica, ACV                                                             | 8    |
| Artritis (≥ 2 articulaciones), Miositis, Hematuria, Proteinuria, Cilindros urinarios, Piuria                                                 | 4    |
| Erupción cutánea, Alopecia, Úlceras orales, Pleuritis, Pericarditis, Fiebre, Trombocitopenia, Leucopenia, Complemento bajo, Anti-DNA elevado | 2    |

*Cálculo*

$$
\text{SLEDAI-2K} = \sum (\text{peso de cada ítem presente})
$$

> *Interpretación general* (Glasgow et al. 2002):
>
> * 0 = inactivo
> * 1–5 = actividad leve
> * 6–10 = moderada
> * > 10 = alta actividad

---

## Pseudocódigo de implementación

```python
def das28_esr(tjc28, sjc28, vsr, gh):
    vsr = vsr if vsr >= 1 else 1
    return 0.56 * sqrt(tjc28) + 0.28 * sqrt(sjc28) + 0.70 * log(vsr) + 0.014 * gh

def das28_crp(tjc28, sjc28, crp, gh):
    return 0.56 * sqrt(tjc28) + 0.28 * sqrt(sjc28) + 0.36 * log(crp + 1) + 0.014 * gh + 0.96

def cdai(tjc28, sjc28, pga, ega):
    return tjc28 + sjc28 + pga + ega

def sdai(tjc28, sjc28, pga, ega, crp):
    return tjc28 + sjc28 + pga + ega + crp

# Para SLEDAI-2K, primero definir un diccionario de pesos:
sle2_weights = {
    'convulsiones':8, 'psicosis':8, 'cerebral':8,
    'vision':8, 'neuropatia':8, 'vasculitis':8,
    'cefalea':8, 'acv':8,
    'artritis':4, 'miositis':4,
    'hematuria':4, 'proteinuria':4, 'cilindros':4, 'piuria':4,
    'rash':2, 'alopecia':2, 'ulceras_orales':2,
    'pleuritis':2, 'pericarditis':2,
    'fiebre':2, 'trombocitopenia':2, 'leucopenia':2,
    'complemento_bajo':2, 'antiDNA':2
}

def sledai_2k(present_items: list[str]):
    return sum(sle2_weights[item] for item in present_items if item in sle2_weights)

```
