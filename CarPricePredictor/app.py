import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Car Price Predictor')

car = pd.read_csv('cleaned_car_data.csv')
model=pickle.load(open('LinearRegressionModel.pkl','rb'))

yearLs = [i for i in range(1900,2023)]
kmsLs = [i for i in range(0,500000,1000)]

company = st.selectbox(
     'Select a Car Company',
     car['company'].unique())
car_model = st.selectbox(
     'Select a Car Model',
     car['name'].unique())
fuel_type = st.selectbox(
     'Select a Car Fuel-Type',
     ('Petrol','Diesel'))
year = st.selectbox(
     'Select a the year when the car was bought',
     yearLs)

kms_driven = st.selectbox(
     'Number of Kms car has been driven',
     kmsLs)

prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,kms_driven,fuel_type]).reshape(1, 5)))

if st.button('Predict Price'):
     st.header(f"₹ {prediction[0].round()}")
else:
     st.write('Waiting...')
