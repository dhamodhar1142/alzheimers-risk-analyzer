import streamlit as st
import matplotlib.pyplot as plt

# Internationalization block
STRINGS = {
    "en": { "app_title": "🧠 Alzheimer's Risk Analyzer", "app_desc": "This tool helps assess potential risk factors for Alzheimer's disease based on age, gender, lifestyle, and other health indicators. Note: This is for educational purposes only and should not replace professional medical advice.",
        "language": "Language",
        "personal_info": "Personal Information", "age": "Age", "gender": "Gender", "male": "Male", "female": "Female", "other": "Other",
        "genetics": "Genetics", "apoe": "APOE ε4 Carrier", "family_history": "Family History of Alzheimer's", "yes": "Yes", "no": "No", "unknown": "Unknown",
        "cardio": "Cardiovascular Health", "bp": "Hypertension", "chol": "High Cholesterol", "afib": "Atrial Fibrillation", "stroke": "History of Stroke",
        "metabolic": "Metabolic Factors", "diabetes": "Diabetes", "obesity": "Obesity", "sleep_apnea": "Sleep Apnea",
        "lifestyle": "Lifestyle", "exercise": "Physical Activity Level", "diet": "Diet Quality", "smoking": "Smoking Status", "alcohol": "Alcohol Consumption",
        "cognitive": "Cognitive/Educational", "education": "Highest Education Level", "cog_activity": "Cognitive/Social Engagement",
        "psychiatric": "Psychiatric", "depression": "History of Depression",
        "neurological": "Neurological", "tbi": "Traumatic Brain Injury (TBI)",
        "sensory": "Sensory Impairment", "hearing": "Hearing Impairment", "vision": "Vision Impairment",
        "environmental": "Environmental", "air_pollution": "Air Pollution Exposure", "pesticides": "Pesticide Exposure",
        "medical": "Major Medical Conditions", "ckd": "Chronic Kidney Disease", "copd": "COPD",
        "analysis": "Risk Analysis & Summary", "submit": "Analyze" },

    "es": { "app_title": "🧠 Analizador de Riesgo de Alzheimer", "app_desc": "Herramienta para evaluar factores de riesgo según edad, género, estilo de vida y salud. Propósito educativo, no sustituye consejo médico.",
        "language": "Idioma",
        "personal_info": "Información personal", "age": "Edad", "gender": "Género", "male": "Hombre", "female": "Mujer", "other": "Otro",
        "genetics": "Genética", "apoe": "Portador de APOE ε4", "family_history": "Antecedentes familiares de Alzheimer", "yes": "Sí", "no": "No", "unknown": "Desconocido",
        "cardio": "Salud cardiovascular", "bp": "Hipertensión", "chol": "Colesterol alto", "afib": "Fibrilación auricular", "stroke": "Antecedentes de accidente cerebrovascular",
        "metabolic": "Factores metabólicos", "diabetes": "Diabetes", "obesity": "Obesidad", "sleep_apnea": "Apnea del sueño",
        "lifestyle": "Estilo de vida", "exercise": "Nivel de actividad física", "diet": "Calidad de la dieta", "smoking": "Tabaquismo", "alcohol": "Consumo de alcohol",
        "cognitive": "Cognitivo/Educativo", "education": "Nivel educativo más alto", "cog_activity": "Compromiso cognitivo/social",
        "psychiatric": "Psiquiátrico", "depression": "Antecedentes de depresión",
        "neurological": "Neurológico", "tbi": "Lesión cerebral traumática (TBI)",
        "sensory": "Discapacidad sensorial", "hearing": "Discapacidad auditiva", "vision": "Discapacidad visual",
        "environmental": "Ambiental", "air_pollution": "Exposición a contaminación del aire", "pesticides": "Exposición a pesticidas",
        "medical": "Condiciones médicas principales", "ckd": "Enfermedad renal crónica", "copd": "EPOC",
        "analysis": "Análisis de riesgo y resumen", "submit": "Analizar" },

    "zh": { "app_title": "🧠 阿尔茨海默病风险分析器", "app_desc": "此工具根据年龄、性别、生活方式和其他健康指标帮助评估阿尔茨海默病的风险。仅用于教育目的，不能替代专业医疗建议。",
        "language": "语言",
        "personal_info": "个人信息", "age": "年龄", "gender": "性别", "male": "男", "female": "女", "other": "其他",
        "genetics": "遗传因素", "apoe": "APOE ε4 携带者", "family_history": "家族史", "yes": "是", "no": "否", "unknown": "不确定",
        "cardio": "心血管健康", "bp": "高血压", "chol": "高胆固醇", "afib": "心房颤动", "stroke": "中风史",
        "metabolic": "代谢因素", "diabetes": "糖尿病", "obesity": "肥胖", "sleep_apnea": "睡眠呼吸暂停",
        "lifestyle": "生活方式", "exercise": "身体活动水平", "diet": "饮食质量", "smoking": "吸烟状况", "alcohol": "饮酒情况",
        "cognitive": "认知/教育", "education": "最高教育程度", "cog_activity": "认知/社交参与",
        "psychiatric": "精神", "depression": "抑郁史",
        "neurological": "神经", "tbi": "外伤性脑损伤",
        "sensory": "感觉障碍", "hearing": "听力障碍", "vision": "视力障碍",
        "environmental": "环境", "air_pollution": "空气污染暴露", "pesticides": "农药暴露",
        "medical": "主要医疗状况", "ckd": "慢性肾病", "copd": "慢性阻塞性肺病",
        "analysis": "风险分析与总结", "submit": "分析" },

    "hi": { "app_title": "🧠 अल्ज़ाइमर जोखिम विश्लेषक", "app_desc": "यह उपकरण आयु, लिंग, जीवनशैली और स्वास्थ्य संकेतकों के आधार पर अल्ज़ाइमर रोग का जोखिम आकलन करता है। केवल शैक्षिक उद्देश्य, चिकित्सा सलाह नहीं।",
        "language": "भाषा",
        "personal_info": "व्यक्तिगत जानकारी", "age": "आयु", "gender": "लिंग", "male": "पुरुष", "female": "महिला", "other": "अन्य",
        "genetics": "आनुवंशिकी", "apoe": "APOE ε4 वाहक", "family_history": "पारिवारिक इतिहास", "yes": "हाँ", "no": "नहीं", "unknown": "अज्ञात",
        "cardio": "हृदय स्वास्थ्य", "bp": "उच्च रक्तचाप", "chol": "उच्च कोलेस्ट्रॉल", "afib": "गर्भाशय फाइब्रिलेशन", "stroke": "स्ट्रोक का इतिहास",
        "metabolic": "चयापचय कारक", "diabetes": "मधुमेह", "obesity": "मोटापा", "sleep_apnea": "स्लीप एपनिया",
        "lifestyle": "जीवनशैली", "exercise": "शारीरिक गतिविधि स्तर", "diet": "आहार गुणवत्ता", "smoking": "धूम्रपान स्थिति", "alcohol": "मद्यपान",
        "cognitive": "संज्ञानात्मक/शैक्षिक", "education": "शिक्षा स्तर", "cog_activity": "संज्ञानात्मक/सामाजिक सहभागिता",
        "psychiatric": "मनोचिकित्सा", "depression": "अवसाद का इतिहास",
        "neurological": "तंत्रिका", "tbi": "आघातजन्य मस्तिष्क चोट",
        "sensory": "संवेदी बाधाएँ", "hearing": "श्रवण बाधा", "vision": "दृष्टि बाधा",
        "environmental": "पर्यावरण", "air_pollution": "वायु प्रदूषण", "pesticides": "कीटनाशक का संपर्क",
        "medical": "मुख्य चिकित्सा स्थितियाँ", "ckd": "क्रोनिक किडनी रोग", "copd": "सीओपीडी",
        "analysis": "जोखिम विश्लेषण और सारांश", "submit": "विश्लेषण करें" }
}

st.set_page_config(page_title="Alzheimer's Risk Analyzer", page_icon="🧠", layout="wide")
lang = st.sidebar.selectbox(
    "Language / भाषा / 语言 / Idioma",
    options=["en", "es", "zh", "hi"],
    format_func=lambda k: {
        "en": "English",
        "es": "Español (Spanish)",
        "zh": "中文 (Chinese)",
        "hi": "हिन्दी (Hindi)"
    }[k]
)
T = STRINGS[lang]

st.title(T["app_title"])
st.write(T["app_desc"])

# Sidebar Risk Inputs
with st.sidebar:
    st.header(T["personal_info"])
    age = st.slider(T["age"], 40, 100, 65)
    gender = st.selectbox(T["gender"], [T["male"], T["female"], T["other"]])

    st.markdown("---")
    st.header(T["genetics"])
    apoe = st.radio(T["apoe"], [T["yes"], T["no"], T["unknown"]])
    family_history = st.radio(T["family_history"], [T["yes"], T["no"], T["unknown"]])

    st.markdown("---")
    st.header(T["cardio"])
    hypertension = st.checkbox(T["bp"])
    cholesterol = st.checkbox(T["chol"])
    afib = st.checkbox(T["afib"])
    stroke = st.checkbox(T["stroke"])

    st.markdown("---")
    st.header(T["metabolic"])
    diabetes = st.checkbox(T["diabetes"])
    obesity = st.checkbox(T["obesity"])
    sleep_apnea = st.checkbox(T["sleep_apnea"])

    st.markdown("---")
    st.header(T["lifestyle"])
    exercise = st.select_slider(T["exercise"], options=[T["unknown"], "None/Minimal", "Light", "Moderate", "High"])
    diet = st.select_slider(T["diet"], options=[T["unknown"], "Poor", "Fair", "Good", "Excellent"])
    smoking = st.radio(T["smoking"], ["Never", "Former", "Current"])
    alcohol = st.selectbox(T["alcohol"], ["None", "Light", "Moderate", "Heavy"])

    st.markdown("---")
    st.header(T["cognitive"])
    education = st.selectbox(T["education"], ["Less than high school", "High school", "Some college/technical", "Bachelor's", "Graduate"])
    cog_social = st.select_slider(T["cog_activity"], options=[T["unknown"], "Low", "Moderate", "High"])

    st.markdown("---")
    st.header(T["psychiatric"])
    depression = st.radio(T["depression"], [T["yes"], T["no"], T["unknown"]])

    st.markdown("---")
    st.header(T["neurological"])
    tbi = st.radio(T["tbi"], [T["yes"], T["no"], T["unknown"]])

    st.markdown("---")
    st.header(T["sensory"])
    hearing_imp = st.radio(T["hearing"], [T["yes"], T["no"], T["unknown"]])
    vision_imp = st.radio(T["vision"], [T["yes"], T["no"], T["unknown"]])

    st.markdown("---")
    st.header(T["environmental"])
    air_pollution = st.radio(T["air_pollution"], [T["yes"], T["no"], T["unknown"]])
    pesticide_exp = st.radio(T["pesticides"], [T["yes"], T["no"], T["unknown"]])

    st.markdown("---")
    st.header(T["medical"])
    ckd = st.checkbox(T["ckd"])
    copd = st.checkbox(T["copd"])

summary = {
    "age": age, "gender": gender, "apoe": apoe, "family_history": family_history,
    "hypertension": hypertension, "cholesterol": cholesterol, "afib": afib, "stroke": stroke,
    "diabetes": diabetes, "obesity": obesity, "sleep_apnea": sleep_apnea,
    "exercise": exercise, "diet": diet, "smoking": smoking, "alcohol": alcohol,
    "education": education, "cog_social": cog_social,
    "depression": depression, "tbi": tbi,
    "hearing_imp": hearing_imp, "vision_imp": vision_imp,
    "air_pollution": air_pollution, "pesticide_exp": pesticide_exp,
    "ckd": ckd, "copd": copd,
}

# Risk Calculation (dummy logic, you can improve!)
def get_risk_score(summary):
    risk = 10
    if summary["apoe"] == T["yes"]: risk += 15
    if summary["family_history"] == T["yes"]: risk += 10
    if summary["diabetes"]: risk += 8
    if summary["hypertension"]: risk += 7
    if summary["exercise"] == "None/Minimal": risk += 8
    if summary["age"] >= 75: risk += 10
    if summary["depression"] == T["yes"]: risk += 7
    return min(risk, 95)

if st.button(T["submit"]):
    st.header(T["analysis"])
    risk_score = get_risk_score(summary)
    # Color code
    color = "green" if risk_score < 25 else ("orange" if risk_score < 50 else ("red" if risk_score < 75 else "darkred"))
    st.markdown(f"<h2 style='color:{color}'>{T['analysis']}<br>Estimated Risk: {risk_score:.1f}%</h2>", unsafe_allow_html=True)

    # Feature importance demo chart (dummy)
    fig, ax = plt.subplots()
    features = ["Genetics", "Age", "Exercise"]
    weights = [15, 10, 8]
    ax.barh(features, weights, color="coral")
    ax.set_xlabel("Risk Points")
    st.pyplot(fig)

    # Personalized advice
    if summary["exercise"] == "None/Minimal":
        st.info("🚶 Increasing your activity level may reduce your risk by up to 40%.")
    if summary["diabetes"]:
        st.info("🩺 Managing your diabetes carefully can lower cognitive decline risk.")
    if summary["depression"] == T["yes"]:
        st.info("🌱 Addressing depression can reduce Alzheimer's risk.")

    # Show inputs summary
    st.json(summary)
