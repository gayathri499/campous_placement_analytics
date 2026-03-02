import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("placement_data.csv")

X = df.drop(["Placement_Status", "Salary_LPA"], axis=1)
y = df["Placement_Status"]

model = RandomForestClassifier()
model.fit(X, y)

st.title("Campus Placement Analytics System")

cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
aptitude = st.slider("Aptitude Score", 40, 100, 60)
communication = st.slider("Communication Score", 40, 100, 60)
technical = st.slider("Technical Score", 40, 100, 60)
internships = st.slider("Internships", 0, 4, 1)
projects = st.slider("Projects", 1, 6, 2)
certifications = st.slider("Certifications", 0, 5, 1)
hackathons = st.slider("Hackathons", 0, 3, 0)

input_data = np.array([[cgpa, aptitude, communication, technical,
                        internships, projects, certifications, hackathons]])

if st.button("Predict Placement"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("High Chance of Placement ✅")
    else:
        st.error("Low Chance of Placement ❌")