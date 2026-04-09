import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('buyuk_model.pkl')

st.title("🤖 Akıllı İK Analiz Sistemi")

with st.form("cv_form"):
    cdi = st.slider("Şehir Gelişmişlik Endeksi", 0.4, 1.0, 0.8)
    gender = st.selectbox("Cinsiyet", [1, 2, 3], format_func=lambda x: {1:'Erkek', 2:'Kadın', 3:'Diğer'}[x])
    edu = st.selectbox("Eğitim Seviyesi", [1, 2, 3, 4, 5], format_func=lambda x: {1:'Mezun', 2:'Y.Lisans', 3:'Lise', 4:'Doktora', 5:'İlkokul'}[x])
    rel_exp = st.selectbox("İlgili Deneyim", [1, 0], format_func=lambda x: "Var" if x==1 else "Yok")
    train_hours = st.number_input("Eğitim Saatleri", 1, 400, 50)
    
    submit = st.form_submit_button("Analiz Et")

if submit:
    girdi = np.array([[cdi, gender, rel_exp, 0, edu, 0, 0, 0, 0, 0, train_hours]])
    tahmin = model.predict(girdi)
    
    if tahmin[0] == 1:
        st.success("Bu aday yeni iş fırsatlarına çok açık! ✅")
    else:
        st.info("Aday mevcut durumunda stabil görünüyor. ❌")
