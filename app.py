import streamlit as st
import pandas as pd
#import numpy_financial as npf

st.title('Retirment Calculator')
age = st.number_input('Enter your age', 10,110,25)
retirement_age = st.number_input('Enter your expected retirement age', 10,110,65)
income = st.number_input("Enter you desired income in retirement in today's dollars", 1000, 10000000,70000, 1000)

#st.write(f'Hello {name}!')
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)