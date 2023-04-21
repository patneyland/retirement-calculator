import streamlit as st
import pandas as pd
import numpy_financial as npf
import humanize

#setting up the web application
st.title('A Better Retirment Calculator')
st.write("Checkout the Github [Repository](https://github.com/patrickneyland/retirement-calculator) for this calculator.")
st.write("This calculator is designed to help you determine how much you need to save for retirement \
    and how much you can withdraw from your nestegg each month.")

my_expander = st.expander(label='Click here to expand explanations of the various assumptions')
with my_expander:

    st.write("Rate of Return - The starting rate of return is based on the historical average of the S&P 500. If you invested money in the S&P500 in 1928, the money you would have today would reflect a 6.6% annual rate of return.")
    st.write("Inflation - The inflation rate in the United States averaged 3.29 percent from 1914 until 2023")
    st.write("Taxes - ")
    st.write("Income in Retirement - ")

advanced_parameters = st.expander(label="Click here to adjust advanced parameters such as tax brackets")
with advanced_parameters:

    cola1, cola2 = st.columns(2)
    with cola1:
    #calculating taxes based on retirement income
        rate_1 = st.number_input("rate 1", 0,100,25,1)/100
        rate_2 = st.number_input("rate 2", 0,100,30,1)/100
        rate_3 = st.number_input("rate 3", 0,100,35,1)/100
    #income limits for tax brackets
    with cola2:
        limit_1 = st.number_input("limit 1", 0,10000000,50000,1000)
        limit_2 = st.number_input("limit 2", 0,10000000,100000,1000)
        st.write("The numeric inputs above create the following tax brackets.")

    income_range_1 = f'Less than ${humanize.intcomma(limit_1)}'
    income_range_2 = f'Between ${humanize.intcomma(limit_1)} and ${humanize.intcomma(limit_2)}'
    income_range_3 = f'Greater than ${humanize.intcomma(limit_2)}'

    tax_table = {
    'Income Range': [income_range_1, income_range_2, income_range_3],
    'Tax Rate': [f'{rate_1*100}%', f'{rate_2*100}%', f'{rate_3*100}%']
    }
    df = pd.DataFrame(tax_table, columns = ['Income Range', 'Tax Rate'])
    st.table(df)


col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Current age', 10,110,25)
    retirement_age = st.number_input('Expected retirement age', 10,110,65)
    life_expectancy = st.number_input('Life expectancy', 10,120,90)

with col2:
    withdrawal_amount = st.number_input("Income goal for retirement", 1000, 10000000, 50000, 1000)
    currently_saved = st.number_input("Current savings investments", 0,10000000,0,1000)

with col3:
    rate = st.number_input("Expected rate of return", 0.0,100.00,7.70,0.10)/100
    inflation = st.number_input("Expected inflation rate", 0.0,100.00,3.3,0.10)/100

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

st.write("You are currently expecting to work for {} more years.".format(work_years))
st.write("To meet retirment income expectations, your nestegg target is ${:,.0f}.".format(nestegg))
st.write("You will need to invest ${:,.2f}".format(monthly_contributions)+" at the end of each month to reach your nestegg goal.")
st.write("You will be able to withdraw ${:,.2f}".format(monthly_withdrawal_amount)+" of todays dollars per month after taxes are paid.")

# import streamlit as st
# import pandas as pd
# import numpy_financial as npf
# import humanize
# import altair as alt

# # Setting up the web application
# st.title('A Better Retirement Calculator')
# st.write("Checkout the Github [Repository](https://github.com/patrickneyland/retirement-calculator) for this calculator.")
# st.write("This calculator is designed to help you determine how much you need to save for retirement \
#     and how much you can withdraw from your nestegg each month.")

# my_expander = st.expander(label='Click here to expand explanations of the various assumptions')
# with my_expander:
#     st.write("Rate of Return - The starting rate of return is based on the historical average of the S&P 500. If you invested money in the S&P500 in 1928, the money you would have today would reflect a 6.6% annual rate of return.")
#     st.write("Inflation - The inflation rate in the United States averaged 3.29 percent from 1914 until 2023")
#     st.write("Taxes - ")
#     st.write("Income in Retirement - ")

# advanced_parameters = st.expander(label="Click here to adjust advanced parameters such as tax brackets")
# with advanced_parameters:
#     cola1, cola2 = st.columns(2)
#     with cola1:
#         # Calculating taxes based on retirement income
#         rate_1 = st.number_input("rate 1", 0, 100, 25, 1) / 100
#         rate_2 = st.number_input("rate 2", 0, 100, 30, 1) / 100
#         rate_3 = st.number_input("rate 3", 0, 100, 35, 1) / 100
#     # Income limits for tax brackets
#     with cola2:
#         limit_1 = st.number_input("limit 1", 0, 10000000, 50000, 1000)
#         limit_2 = st.number_input("limit 2", 0, 10000000, 100000, 1000)
#         st.write("The numeric inputs above create the following tax brackets.")

#     income_range_1 = f'Less than ${humanize.intcomma(limit_1)}'
#     income_range_2 = f'Between ${humanize.intcomma(limit_1)} and ${humanize.intcomma(limit_2)}'
#     income_range_3 = f'Greater than ${humanize.intcomma(limit_2)}'

#     tax_table = {
#         'Income Range': [income_range_1, income_range_2, income_range_3],
#         'Tax Rate': [f'{rate_1 * 100}%', f'{rate_2 * 100}%', f'{rate_3 * 100}%']
#     }
#     df = pd.DataFrame(tax_table, columns=['Income Range', 'Tax Rate'])
#     st.table(df)

# col1, col2, col3 = st.columns(3)

# with col1:
#     age = st.number_input('Current age', 10, 110, 25)
#     retirement_age = st.number_input('Expected retirement age', 10, 110, 65)
#     life_expectancy = st.number_input('Life expectancy', 10, 120, 90)

# with col2:
#     withdrawal_amount = st.number_input("Income goal for retirement", 1000, 10000000, 50000, 1000)
#     currently_saved = st.number_input("Current savings investments", 0, 10000000, 0, 1000)

# with col3:
#     rate = st.number_input("Expected rate of return", 0.0, 100.00, 7.70, 0.10) / 100
#     inflation = st.number_input("Expected inflation rate", 0.0, 100.00, 3.3, 0.10) / 100

# real_rate = (1 + rate) / (1 + inflation) - 1
# monthly_withdrawal_amount = withdrawal_amount / 12
# work_years = retirement_age - age
# retirement_years = life_expectancy - retirement_age

# if withdrawal_amount <= limit_1:
#     tax_adjusted_withdrawal_amount = withdrawal_amount / (1 - rate_1)
# elif withdrawal_amount <= limit_2:
#     tax_adjusted_withdrawal_amount = (withdrawal_amount - limit_1) / (1 - rate_2) + limit_1 / (1 - rate_1)
# else:
#     tax_adjusted_withdrawal_amount = (withdrawal_amount - limit_2) / (1 - rate_3) + limit_1 / (1 - rate_1) + (limit_2 - limit_1) / (1 - rate_2)

# nestegg = npf.pv(real_rate / 12, retirement_years * 12, -tax_adjusted_withdrawal_amount / 12, 0, when='begin')

# monthly_contributions = npf.pmt(real_rate / 12, work_years * 12, currently_saved, -nestegg)

# st.write("You are currently expecting to work for {} more years.".format(work_years))
# st.write("To meet retirement income expectations, your nestegg target is ${:,.0f}.".format(nestegg))
# st.write("You will need to invest ${:,.2f}".format(monthly_contributions) + " at the end of each month to reach your nestegg goal.")
# st.write("You will be able to withdraw ${:,.2f}".format(monthly_withdrawal_amount) + " of today's dollars per month after taxes are paid.")

# # # Create a dataframe for the Altair chart
# # data = pd.DataFrame({'Year': range(age, life_expectancy + 1)})
# # data['Savings'] = [npf.fv(real_rate / 12, (year - age) * 12, -monthly_contributions, currently_saved) for year in data['Year']]
# # data['Withdrawals'] = [min(npf.pv(real_rate / 12, (life_expectancy - year) * 12, -tax_adjusted_withdrawal_amount / 12, 0, when='begin'), saving) for year, saving in zip(data['Year'], data['Savings'])]

# # # Create the Altair chart
# # chart = alt.Chart(data).mark_area(opacity=0.5).encode(
# #     alt.X('Year:Q', axis=alt.Axis(title='Age')),
# #     alt.Y('Savings:Q', axis=alt.Axis(title='Savings and Withdrawals')),
# #     alt.Color('key:N', legend=alt.Legend(title='Key')),
# #     order='key:N'
# # ).transform_fold(
# #     ['Savings', 'Withdrawals']
# # )

# # st.altair_chart(chart, use_container_width=True)

# # Calculate the savings and withdrawals for each year
# # Calculate the retirement account balance for each year
# years = list(range(age, life_expectancy + 1))
# retirement_account_balance = []

# for year in years:
#     if year < retirement_age:
#         balance = npf.fv(rate / 12, (year - age) * 12, -monthly_contributions, currently_saved)
#     else:
#         balance = npf.fv(real_rate / 12, (year - retirement_age) * 12, -tax_adjusted_withdrawal_amount / 12, nestegg)
#     retirement_account_balance.append(max(0, balance))

# # Create a data frame to store the retirement account balance data
# data = pd.DataFrame({'Year': years, 'Retirement Account Balance': retirement_account_balance})

# # Create an Altair line chart to visualize the retirement account balance
# chart = alt.Chart(data).mark_line().encode(
#     x='Year:Q',
#     y='Retirement Account Balance:Q'
# )

# st.altair_chart(chart, use_container_width=True)