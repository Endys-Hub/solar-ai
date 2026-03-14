import streamlit as st
import joblib
import numpy as np

model = joblib.load("../src/solar_model.pkl")

st.title("SolarSense AI")

sunlight = st.slider("Sunlight Hours",0,12,6)
temperature = st.slider("Temperature (°C)",15,40,30)

prediction = model.predict([[sunlight,temperature]])

st.write("Predicted Solar Output:", round(prediction[0],2),"kWh")

if sunlight >= 6:
    st.success("Good time to run heavy appliances.")
else:
    st.warning("Solar output may be low.")

# streamlit run streamlit_app.py