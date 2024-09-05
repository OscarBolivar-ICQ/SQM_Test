import streamlit as st
import joblib
import numpy as np

# Load the trained XGBoost model
model = joblib.load('Clasificador_Pozas.pkl')

# Define a function to make predictions
def predict_pond_type(input_data):
    # Reshape the input data to match the model's expected input shape
    input_data = np.array(input_data).reshape(1, -1)
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Convert numerical predictions back to labels
    pond_types = ['Carnalita K', 'Halita', 'Kainita|Schoenita', 'Li2SO4', 'Silvinita']
    return pond_types[int(prediction)]

# Streamlit App UI
st.title("Clasificación de Pozas Basado en Químicas de Poza")

st.write("Ingresa Químicas para Clasificar la Poza:")

# Input fields for chemical composition values
k = st.number_input('% K', value=0.0, step=0.01)
na = st.number_input('% Na', value=0.0, step=0.01)
mg = st.number_input('% Mg', value=0.0, step=0.01)
ca = st.number_input('% Ca', value=0.0, step=0.01)
so4 = st.number_input('% SO4', value=0.0, step=0.01)
li = st.number_input('% Li', value=0.0, step=0.01)
cl = st.number_input('% Cl', value=0.0, step=0.01)
h3bo3 = st.number_input('% H3BO3', value=0.0, step=0.01)

# Automatically calculate Mg_rounded
mg_rounded = round(mg, 2)

# When the user clicks the "Predict" button
if st.button("Predecir Tipo de Poza"):
    # Collect the input data into a list, including Mg_rounded
    input_data = [k, na, mg, mg_rounded, ca, so4, li, cl, h3bo3]
    
    # Make prediction
    result = predict_pond_type(input_data)
    
    # Display the result
    st.success(f"Resultado de Predicción: Esta Poza Corresponde a una de {result}")