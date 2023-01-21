import streamlit as st
import pandas as pd
import numpy_financial as npf

st.title('Retirment Calculator')
name = st.text_input('Enter your name', '')
age = st.number_input('Enter your Age', 10,110)

st.write(f'Hello {name}!')
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)