import streamlit as st
import pandas as pd
import numpy_financial as npf

st.title('Retirment Calculator')
age = st.number_input('Enter your age', 10,110,25)
retirement_age = st.number_input('Enter your expected retirement age', 10,110,65)
income = st.number_input("Enter you desired income in retirement in today's dollars", 1000, 10000000,70000, 1000)
pmt = st.number_input('Enter monthly contribution', 100,1000000,100)

#st.write(f'Hello {name}!')
x = npf.fv(.1,retirement_age-age,-pmt,0)
#y = st.slider('Select an integer y', 0, 10, 1)
st.title('At age 65, you will have' + x)

#df = pd.DataFrame({'PV': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
#st.write(df)