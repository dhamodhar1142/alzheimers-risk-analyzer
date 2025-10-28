import streamlit as st
import pandas as pd
import numpy as np

# ---------------- Page configuration ----------------
st.set_page_config(page_title="Alzheimer's Risk Analyzer", page_icon="🧠", layout="wide")

# ---------------- i18n strings ----------------
STRINGS = {
    "en": {"app_title": "🧠 Alzheimer's Risk Analyzer","app_desc": "This tool helps assess potential risk factors for Alzheimer's disease based on age, gender, lifestyle, and other health indicators. Note: This is for educational purposes only and should not replace professional medical advice.","language": "Language","personal_info": "Personal Information","age": "Age","gender": "Gender","male": "Male","female": "Female","other": "Other","genetics": "Genetics","apoe": "APOE ε4 Carrier","family_history": "Family History of Alzheimer's","yes": "Yes","no": "No","unknown": "Unknown","cardio": "Cardiovascular Health","bp": "Hypertension (High Blood Pressure)","chol": "High Cholesterol","afib": "Atrial Fibrillation","stroke": "History of Stroke","metabolic": "Metabolic Factors","diabetes": "Diabetes","obesity": "Obesity (BMI ≥ 30)","sleep_apnea": "Sleep Apnea","lifestyle": "Lifestyle","exercise": "Physical Activity Level","diet": "Diet Quality","smoking": "Smoking Status","alcohol": "Alcohol Consumption","cognitive": "Cognitive/Educational","education": "Highest Education Level","cog_activity": "Cognitive/Social Engagement","psychiatric": "Psychiatric","depression": "History of Depression","neurological": "Neurological","tbi": "Traumatic Brain Injury (TBI)","sensory": "Sensory Impairment","hearing": "Hearing Impairment","vision": "Vision Impairment","environmental": "Environmental","air_pollution": "High Air Pollution Exposure","pesticides": "Significant Pesticide Exposure","medical": "Major Medical Conditions","ckd": "Chronic Kidney Disease","copd": "COPD/Chronic Respiratory Disease","analysis": "Risk Inputs Summary","submit": "Analyze",},
    "es": {"app_title": "🧠 Analizador de Riesgo de Alzheimer","app_desc": "Esta herramienta ayuda a evaluar factores de riesgo potenciales de la enfermedad de Alzheimer según edad, género, estilo de vida y otros indicadores de salud. Nota: Solo con fines educativos; no reemplaza el consejo médico profesional.","language": "Idioma","personal_info": "Información personal","age": "Edad","gender": "Género","male": "Hombre","female": "Mujer","other": "Otro","genetics": "Genética","apoe": "Portador de APOE ε4","family_history": "Antecedentes familiares de Alzheimer","yes": "Sí","no": "No","unknown": "Desconocido","cardio": "Salud cardiovascular","bp": "Hipertensión (presión alta)","chol": "Colesterol alto","afib": "Fibrilación auricular","stroke": "Antecedente de accidente cerebrovascular","metabolic": "Factores metabólicos","diabetes": "Diabetes","obesity": "Obesidad (IMC ≥ 30)","sleep_apnea": "Apnea del sueño","lifestyle": "Estilo de vida","exercise": "Nivel de actividad física","diet": "Calidad de la dieta","smoking": "Tabaquismo","alcohol": "Consumo de alcohol","cognitive": "Cognitivo/Educativo","education": "Nivel educativo más alto","cog_activity": "Compromiso cognitivo/social","psychiatric": "Psiquiátrico","depression": "Antecedente de depresión","neurological": "Neurológico","tbi": "Lesión cerebral traumática (TBI)","sensory": "Discapacidad sensorial","hearing": "Discapacidad auditiva","vision": "Discapacidad visual","environmental": "Ambiental","air_pollution": "Alta exposición a contaminación del aire","pesticides": "Exposición significativa a pesticidas","medical": "Condiciones médicas principales","ckd": "Enfermedad renal crónica","copd": "EPOC/Enfermedad respiratoria crónica","analysis": "Resumen de entradas de riesgo","submit": "Analizar",},
    "zh": {"app_title": "🧠 阿尔茨海默病风险分析器","app_desc": "此工具根据年龄、性别、生活方式和其他健康指标帮助评估阿尔茨海默病的潜在风险因素。注意：仅用于教育目的，不能替代专业医疗建议。","language": "语言","personal_info": "个人信息","age": "年龄","gender": "性别","male": "男","female": "女","other": "其他","genetics": "遗传因素","apoe": "APOE ε4 携带者","family_history": "阿尔茨海默病家族史","yes": "是","no": "否","unknown": "不确定","cardio": "心血管健康","bp": "高血压","chol": "高胆固醇","afib": "心房颤动","stroke": "中风史","metabolic": "代谢因素","diabetes": "糖尿病","obesity": "肥胖（BMI ≥ 30）","sleep_apnea": "睡眠呼吸暂停","lifestyle": "生活方式","exercise": "身体活动水平","diet": "饮食质量","smoking": "吸烟状况","alcohol": "饮酒情况","cognitive": "认知/教育","education": "最高教育程度","cog_activity": "认知/社交参与","psychiatric": "精神科","depression": "抑郁史","neurological": "神经科","tbi": "外伤性脑损伤","sensory": "感觉障碍","hearing": "听力障碍","vision": "视力障碍","environmental": "环境","air_pollution": "高空气污染暴露","pesticides": "显著的农药暴露","medical": "主要医疗状况","ckd": "慢性肾病","copd": "慢性阻塞性肺病/慢性呼吸系统疾病","analysis": "风险输入摘要","submit": "分析",},
    "hi": {"app_title": "🧠 अल्ज़ाइमर जोखिम विश्लेषक","app_desc": "यह उपकरण आयु, लिंग, जीवनशैली और अन्य स्वास्थ्य संकेतकों के आधार पर अल्ज़ाइमर रोग के संभावित जोखिम कारकों का आकलन करने में मदद करता है। ध्यान दें: यह केवल शैक्षिक उद्देश्यों के लिए है और चिकित्सा सलाह का विकल्प नहीं है।","language": "भाषा","personal_info": "व्यक्तिगत जानकारी","age": "आयु","gender": "लिंग","male": "पुरुष","female": "महिला","other": "अन्य","genetics": "आनुवंशिकी","apoe": "APOE ε4 वाहक","family_history": "अल्ज़ाइमर का पारिवारिक इतिहास","yes": "हाँ","no": "नहीं","unknown": "अज्ञात","cardio": "हृदय-वाहिकीय स्वास्थ्य","bp": "उच्च रक्तचाप","chol": "उच्च कोलेस्ट्रॉल","afib": "एट्रियल फ़िब्रिलेशन","stroke": "स्ट्रोक का इतिहास","metabolic": "चयापचय कारक","diabetes": "मधुमेह","obesity": "मोटापा (BMI ≥ 30)","sleep_apnea": "स्लीप एपनिया","lifestyle": "जीवनशैली","exercise": "शारीरिक गतिविधि स्तर","diet": "आहार की गुणवत्ता","smoking": "धूम्रपान स्थिति","alcohol": "मद्यपान","cognitive": "संज्ञानात्मक/शैक्षिक","education": "सर्वोच्च शिक्षा स्तर","cog_activity": "संज्ञानात्मक/सामाजिक सहभागिता","psychiatric": "मनोचिकित्सा","depression": "अवसाद का इतिहास","neurological": "तंत्रिका संबंधी","tbi": "आघातजन्य मस्तिष्क चोट (TBI)","sensory": "संवेदी हानि","hearing": "श्रवण हानि","vision": "दृष्टि हानि","environmental": "पर्यावरणीय","air_pollution": "उच्च वायु प्रदूषण संपर्क","pesticides": "महत्वपूर्ण कीटनाशक संपर्क","medical": "मुख्य चिकित्सा स्थितियां","ckd": "क्रोनिक किडनी रोग","copd": "सीओपीडी/क्रोनिक श्वसन रोग","analysis": "जोखिम इनपुट सारांश","submit": "विश्लेषण करें",},
    "ar": {"app_title": "🧠 محلل مخاطر الزهايمر","app_desc": "تساعد هذه الأداة في تقييم عوامل الخطر المحتملة لمرض الزهايمر بناءً على العمر والجنس ونمط الحياة ومؤشرات صحية أخرى. ملاحظة: لأغراض تعليمية فقط ولا تغني عن الاستشارة الطبية.","language": "اللغة","personal_info": "معلومات شخصية","age": "العمر","gender": "النوع","male": "ذكر","female": "أنثى","other": "آخر","genetics": "عوامل وراثية","apoe": "حامل APOE ε4","family_history": "تاريخ عائلي لمرض الزهايمر","yes": "نعم","no": "لا","unknown": "غير معروف","cardio": "الصحة القلبية الوعائية","bp": "ارتفاع ضغط الدم","chol": "ارتفاع الكوليسترول","afib": "رجفان أذيني","stroke": "سجل سكتة دماغية","metabolic": "عوامل أيضية","diabetes": "داء السكري","obesity": "السمنة (BMI ≥ 30)","sleep_apnea": "انقطاع النفس أثناء النوم","lifestyle": "نمط الحياة","exercise": "مستوى النشاط البدني","diet": "جودة النظام الغذائي","smoking": "التدخين","alcohol": "الكحول","cognitive": "معرفي/تعليمي","education": "أعلى مستوى تعليمي","cog_activity": "الانخراط المعرفي/الاجتماعي","psychiatric": "نفسي","depression": "تاريخ الاكتئاب","neurological": "عصبي","tbi": "إصابة دماغية رضّية","sensory": "ضعف حسي","hearing": "ضعف السمع","vision": "ضعف البصر","environmental": "بيئي","air_pollution": "تعرض مرتفع لتلوث الهواء","pesticides": "تعرض كبير للمبيدات","medical": "حالات طبية كبرى","ckd": "مرض الكلى المزمن","copd": "داء الانسداد الرئوي المزمن/مرض تنفسي مزمن","analysis": "ملخص مُدخلات المخاطر","submit": "تحليل",},
}

# ---------------- Language selection ----------------
st.sidebar.header(STRINGS["en"]["language"])  # label for selector
lang = st.sidebar.selectbox(" ", options=["en", "es", "zh", "hi", "ar"], format_func=lambda k: STRINGS[k]["language"])
T = STRINGS[lang]

# ---------------- UI ----------------
st.title(T["app_title"])
st.write(T["app_desc"])

# Personal info
st.sidebar.header(T["personal_info"])
age = st.sidebar.slider(T["age"], 40, 100, 65)
gender = st.sidebar.selectbox(T["gender"], [T["male"], T["female"], T["other"]])

# Genetics
st.sidebar.header(T["genetics"])
apoe = st.sidebar.radio(T["apoe"], [T["yes"], T["no"], T["unknown"]])
family_history = st.sidebar.radio(T["family_history"], [T["yes"], T["no"], T["unknown"]])

# Cardiovascular
st.sidebar.header(T["cardio"])
hypertension = st.sidebar.checkbox(T["bp"])
cholesterol = st.sidebar.checkbox(T["chol"])
afib = st.sidebar.checkbox(T["afib"])
stroke = st.sidebar.checkbox(T["stroke"])

# Metabolic
st.sidebar.header(T["metabolic"])
diabetes = st.sidebar.checkbox(T["diabetes"])
obesity = st.sidebar.checkbox(T["obesity"])
sleep_apnea = st.sidebar.checkbox(T["sleep_apnea"])

# Lifestyle
st.sidebar.header(T["lifestyle"])
exercise = st.sidebar.select_slider(T["exercise"], options=[T["unknown"], "None/Minimal", "Light", "Moderate", "High"])
diet = st.sidebar.select_slider(T["diet"], options=[T["unknown"], "Poor", "Fair", "Good", "Excellent"])
smoking = st.sidebar.radio(T["smoking"], ["Never", "Former", "Current"])
alcohol = st.sidebar.selectbox(T["alcohol"], ["None", "Light", "Moderate", "Heavy"])

# Cognitive/Educational
st.sidebar.header(T["cognitive"])
education = st.sidebar.selectbox(T["education"], ["Less than high school", "High school", "Some college/technical", "Bachelor's", "Graduate"])
cog_social = st.sidebar.select_slider(T["cog_activity"], options=[T["unknown"], "Low", "Moderate", "High"])

# Psychiatric
st.sidebar.header(T["psychiatric"])
depression = st.sidebar.radio(T["depression"], [T["yes"], T["no"], T["unknown"]])

# Neurological
st.sidebar.header(T["neurological"])
tbi = st.sidebar.radio(T["tbi"], [T["yes"], T["no"], T["unknown"]])

# Sensory impairment
st.sidebar.header(T["sensory"])
hearing_imp = st.sidebar.radio(T["hearing"], [T["yes"], T["no"], T["unknown"]])
vision_imp = st.sidebar.radio(T["vision"], [T["yes"], T["no"], T["unknown"]])

# Environmental
st.sidebar.header(T["environmental"])
air_pollution = st.sidebar.radio(T["air_pollution"], [T["yes"], T["no"], T["unknown"]])
pesticide_exp = st.sidebar.radio(T["pesticides"], [T["yes"], T["no"], T["unknown"]])

# Major medical
st.sidebar.header(T["medical"])
ckd = st.sidebar.checkbox(T["ckd"])
copd = st.sidebar.checkbox(T["copd"])

# Summary panel
st.header(T["analysis"])
summary = {
    "age": age,
    "gender": gender,
    "apoe": apoe,
    "family_history": family_history,
    "hypertension": hypertension,
    "cholesterol": cholesterol,
    "afib": afib,
    "stroke": stroke,
    "diabetes": diabetes,
    "obesity": obesity,
    "sleep_apnea": sleep_apnea,
    "exercise": exercise,
    "diet": diet,
    "smoking": smoking,
    "alcohol": alcohol,
    "education": education,
    "cog_social": cog_social,
    "depression": depression,
    "tbi": tbi,
    "hearing_imp": hearing_imp,
    "vision_imp": vision_imp,
    "air_pollution": air_pollution,
    "pesticide_exp": pesticide_exp,
    "ckd": ckd,
    "copd": copd,
}
st.json(summary)
