import streamlit as st
import pandas as pd
import numpy_financial as npf

#setting up the web application
st.title('Retirment Calculator')
st.write("Checkout the Github [Repository](https://github.com/patrickneyland/retirement-calculator)")


col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Current age', 10,110,25)
    retirement_age = st.number_input('Expected retirement age', 10,110,65)
    life_expectancy = st.number_input('Life expectancy', 10,120,90)

with col2:
    withdrawal_amount = st.number_input("Income goal for retirement", 1000, 10000000, 50000, 1000)
    currently_saved = st.number_input("Current savings investments", 0,10000000,0,1000)

with col3:
    rate = st.number_input("Expected rate of return", 0.0,100.00,6.60,0.10)/100
    inflation = st.number_input("Expected inflation rate", 0.0,100.00,2.8,0.10)/100

#calculating taxes based on retirement income
rate_1 = .25
rate_2 = .30
rate_3 = .35
#income limits for tax brackets
limit_1 = 50000
limit_2 = 100000

real_rate = (1+rate)/(1+inflation)-1
monthly_withdrawal_amount = withdrawal_amount/12
work_years = retirement_age-age
retirement_years = life_expectancy-retirement_age

if withdrawal_amount <= limit_1:
    tax_adjusted_withdrawal_amount = withdrawal_amount/(1-rate_1)
elif withdrawal_amount <= limit_2:
    tax_adjusted_withdrawal_amount = (withdrawal_amount-limit_1)/(1-rate_2) + limit_1/(1-rate_1)
else:
    tax_adjusted_withdrawal_amount = (withdrawal_amount-limit_2)/(1-rate_3) + limit_1/(1-rate_1) + (limit_2-limit_1)/(1-rate_2)

nestegg = npf.pv(real_rate/12, retirement_years*12, -tax_adjusted_withdrawal_amount/12, 0, when='begin')

monthly_contributions = npf.pmt(real_rate/12, work_years*12, currently_saved, -nestegg)

st.write("You are currently expecting to work for {} years".format(work_years))
st.write("Your nestegg target is ${:,.0f}".format(nestegg))
st.write("You will need to invest ${:,.2f}".format(monthly_contributions)+" at the end of each month to reach your nestegg goal.")
st.write("You will be able to withdraw ${:,.2f}".format(monthly_withdrawal_amount)+" of todays dollars per month after taxes are paid.")



