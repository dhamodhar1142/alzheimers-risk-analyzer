import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Alzheimer's Risk Analyzer",
    page_icon="🧠",
    layout="wide"
)

# Title and description
st.title("🧠 Alzheimer's Risk Analyzer")
st.write("""This tool helps assess potential risk factors for Alzheimer's disease based on age, 
gender, lifestyle, and other health indicators. **Note: This is for educational purposes only 
and should not replace professional medical advice.**""")

# Sidebar for user inputs
st.sidebar.header("Personal Information")

# Age input
age = st.sidebar.slider("Age", 40, 100, 65)

# Gender input
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])

# Family history
family_history = st.sidebar.radio("Family History of Alzheimer's", ["Yes", "No", "Unknown"])

# Lifestyle factors
st.sidebar.header("Lifestyle Factors")
exercise = st.sidebar.select_slider("Exercise Frequency", options=["Never", "Rarely", "Sometimes", "Often", "Daily"])
smoking = st.sidebar.radio("Smoking Status", ["Never", "Former", "Current"])
alcohol = st.sidebar.selectbox("Alcohol Consumption", ["None", "Light", "Moderate", "Heavy"])

# Health indicators
st.sidebar.header("Health Indicators")
diabetes = st.sidebar.checkbox("Diabetes")
hypertension = st.sidebar.checkbox("High Blood Pressure")
heart_disease = st.sidebar.checkbox("Heart Disease")
depression = st.sidebar.checkbox("History of Depression")
head_injury = st.sidebar.checkbox("History of Head Injury")

# Cognitive and lifestyle
st.sidebar.header("Cognitive & Lifestyle")
education = st.sidebar.selectbox("Education Level", ["High School or Less", "Some College", "Bachelor's Degree", "Graduate Degree"])
social_activity = st.sidebar.select_slider("Social Activity Level", options=["Low", "Moderate", "High"])
sleep_quality = st.sidebar.select_slider("Sleep Quality", options=["Poor", "Fair", "Good", "Excellent"])

# Calculate risk score
def calculate_risk_score():
    score = 0
    
    # Age factor (most significant)
    if age < 65:
        score += 1
    elif age < 75:
        score += 3
    elif age < 85:
        score += 5
    else:
        score += 7
    
    # Gender (slightly higher risk for females after 65)
    if gender == "Female" and age > 65:
        score += 1
    
    # Family history (significant risk factor)
    if family_history == "Yes":
        score += 4
    elif family_history == "Unknown":
        score += 1
    
    # Lifestyle factors
    exercise_scores = {"Never": 3, "Rarely": 2, "Sometimes": 1, "Often": 0, "Daily": -1}
    score += exercise_scores[exercise]
    
    smoking_scores = {"Current": 2, "Former": 1, "Never": 0}
    score += smoking_scores[smoking]
    
    alcohol_scores = {"Heavy": 2, "Moderate": 0, "Light": 0, "None": 0}
    score += alcohol_scores[alcohol]
    
    # Health conditions
    if diabetes:
        score += 2
    if hypertension:
        score += 1
    if heart_disease:
        score += 2
    if depression:
        score += 1
    if head_injury:
        score += 2
    
    # Protective factors
    education_scores = {"High School or Less": 2, "Some College": 1, "Bachelor's Degree": 0, "Graduate Degree": -1}
    score += education_scores[education]
    
    social_scores = {"Low": 2, "Moderate": 1, "High": 0}
    score += social_scores[social_activity]
    
    sleep_scores = {"Poor": 2, "Fair": 1, "Good": 0, "Excellent": -1}
    score += sleep_scores[sleep_quality]
    
    return max(0, score)  # Ensure score is not negative

# Display results
if st.sidebar.button("Analyze Risk", type="primary"):
    risk_score = calculate_risk_score()
    
    # Create columns for results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Risk Assessment")
        
        # Determine risk level
        if risk_score < 8:
            risk_level = "Low"
            color = "green"
            message = "Your risk factors are relatively low. Continue maintaining a healthy lifestyle!"
        elif risk_score < 15:
            risk_level = "Moderate"
            color = "orange"
            message = "You have some risk factors. Consider discussing prevention strategies with your healthcare provider."
        else:
            risk_level = "High"
            color = "red"
            message = "You have several risk factors. It's important to consult with a healthcare professional for proper evaluation and prevention strategies."
        
        st.markdown(f"### Risk Level: :{color}[{risk_level}]")
        st.metric("Risk Score", f"{risk_score}/30")
        st.info(message)
    
    with col2:
        st.subheader("Your Profile Summary")
        st.write(f"**Age:** {age} years")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Family History:** {family_history}")
        st.write(f"**Exercise:** {exercise}")
        st.write(f"**Education:** {education}")
        st.write(f"**Social Activity:** {social_activity}")
    
    st.divider()
    
    # Recommendations
    st.subheader("📋 Recommendations for Brain Health")
    
    recommendations = []
    
    if exercise in ["Never", "Rarely", "Sometimes"]:
        recommendations.append("🏃 **Increase Physical Activity**: Aim for at least 150 minutes of moderate exercise per week.")
    
    if smoking == "Current":
        recommendations.append("🚭 **Quit Smoking**: Smoking is a significant risk factor for cognitive decline.")
    
    if social_activity == "Low":
        recommendations.append("👥 **Enhance Social Engagement**: Regular social interaction helps maintain cognitive function.")
    
    if sleep_quality in ["Poor", "Fair"]:
        recommendations.append("😴 **Improve Sleep Quality**: Aim for 7-9 hours of quality sleep per night.")
    
    if education == "High School or Less":
        recommendations.append("📚 **Engage in Cognitive Activities**: Reading, puzzles, and learning new skills can help.")
    
    if diabetes or hypertension or heart_disease:
        recommendations.append("❤️ **Manage Chronic Conditions**: Work with your doctor to control diabetes, blood pressure, and heart disease.")
    
    recommendations.extend([
        "🥗 **Follow a Mediterranean Diet**: Rich in fruits, vegetables, whole grains, and healthy fats.",
        "🧘 **Manage Stress**: Practice relaxation techniques like meditation or yoga.",
        "🧠 **Stay Mentally Active**: Engage in activities that challenge your brain.",
        "👨‍⚕️ **Regular Check-ups**: Consult with healthcare providers for regular cognitive assessments."
    ])
    
    for rec in recommendations:
        st.markdown(rec)

else:
    st.info("👈 Please fill in the information on the sidebar and click 'Analyze Risk' to see your results.")

# Footer
st.divider()
st.caption("""**Disclaimer**: This tool is for educational and informational purposes only. It does not provide 
medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical advice.""")
