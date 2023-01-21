import streamlit as st
import pandas as pd
import numpy_financial as npf




st.title('Retirment Calculator')


import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Current age', 10,110,25)
    retirement_age = st.number_input('Expected retirement age', 10,110,65)
    life_expectancy = st.number_input('Life expectancy', 10,120,95)

with col2:
    income = st.number_input("Income goal for retirement", 
        1000, 10000000,70000, 1000)
    currently_saved = st.number_input("Current savings investments", 0,10000000,0,1000)

with col3:
    return_rate = st.number_input("Expected rate of return", 0.0,100.00,11.00,0.10)
    inflation_rate = st.number_input("Expected inflation rate", 0.0,100.00,2.5,0.10)


working_years = retirement_age-age
retirement_years = life_expectancy-retirement_age


df = pd.DataFrame({'Time': [x for x in range(working_years+retirement_years)],
                    'Age': [age + x for x in range(working_years+retirement_years)],
                    'Goal income': [income*(1+(inflation_rate/100))* x for x in range(working_years+retirement_years)]})
st.write(df)

#    def income(t):
 #       return (t*0.0315 + t**2*-0.00062)*60_000
#
  #  data = {'Year': [2022 + x for x in range(years+retirement_years)],
 #           'Age': [age_start + x for x in range(years+retirement_years)],
 #           'income': [income_start+income(x) if x<years else 0 for x in range(years+retirement_years)],



#pmt = st.number_input('Enter monthly contribution', 100,1000000,100)

#st.write(f'Hello {name}!')
#x = round(npf.fv(.1,working_years,-pmt,0),2)
#y = st.slider('Select an integer y', 0, 10, 1)
#st.title('At age 65, you will have...')
#st.title(x)

#df = pd.DataFrame({'PV': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
#st.write(df)