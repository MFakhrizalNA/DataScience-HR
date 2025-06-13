import streamlit as st
import pandas as pd
import joblib

# Load model dan scaler
model = joblib.load('model_random_forest_classifier.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Prediksi Karyawan Keluar")

# Input dari user
job_role = st.selectbox("Job Role", [
    "Lainnya", "Laboratory Technician", "Manager", 
    "Manufacturing Director", "Research Director", 
    "Sales Representative"
])
marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
overtime = st.selectbox("Lembur", ["Yes", "No"])

# Proses input ke format model
# Inisialisasi semua fitur dengan 0
data = {
    'JobRole_Laboratory Technician': 0,
    'JobRole_Manager': 0,
    'JobRole_Manufacturing Director': 0,
    'JobRole_Research Director': 0,
    'JobRole_Sales Representative': 0,
    'MaritalStatus_Single': 0,
    'OverTime_Yes': 0
}

# Isi nilai sesuai input user
if job_role in data:
    data[job_role] = 1
data['MaritalStatus_Single'] = 1 if marital_status == "Single" else 0
data['OverTime_Yes'] = 1 if overtime == "Yes" else 0

# Buat DataFrame dan sesuaikan urutan kolom
input_df = pd.DataFrame([data], columns=[
    'JobRole_Laboratory Technician',
    'JobRole_Manager',
    'JobRole_Manufacturing Director',
    'JobRole_Research Director',
    'JobRole_Sales Representative',
    'MaritalStatus_Single',
    'OverTime_Yes'
])

# Scaling
input_scaled = scaler.transform(input_df)

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"Hasil Prediksi: {'Keluar' if prediction == 1 else 'Tidak Keluar'}")