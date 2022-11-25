import pickle
import streamlit as st

mokas_model = pickle.load(open('usedcar_model2.sav', 'rb'))

st.title('Used Car Price Prediction with KNN')

year = st.text_input('Input Car Year')
mileage = st.text_input('Input Car Mileage')
tax = st.text_input('Input Car Tax')
mpg = st.text_input('Input Car Gas Average Needs')
engineSize = st.text_input('Input Size of Car Engine')

mokas_predict = ''

if st.button('Predict NOW'):
    mokas_predict = mokas_model.predict(
        [[year, mileage, tax, mpg, engineSize]])
    st.write('Predicted Car Price in EUR : ', mokas_predict)
    st.write('Predicted Car Price in IDR (Juta) : ', mokas_predict*19110*1e-6)
