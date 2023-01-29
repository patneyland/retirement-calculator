import streamlit as st
import pandas as pd
import numpy_financial as npf
#import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

#setting up the web application
st.title('Retirment Calculator')
st.write("Checkout the Github [Repository](https://github.com/patrickneyland/retirement-calculator)")


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
rows = working_years+retirement_years
snp_rates = pd.read_csv("S&P500 Historical Annual Returns.csv")

#def incomes(t):
#    return (1+(t*inflation_rate/100))

#incomes = []
#incomes.append(income)


df = pd.DataFrame({'Time': [x for x in range(rows)],
                    'Age': [age + x for x in range(rows)],
                    'Goal income num': [round(income*(1+(inflation_rate/100))**t) for t in range(rows)],
                    'S&P500 Year' : snp_rates['Year'].head(rows),
                    'S&P500 Historical Returns' : snp_rates['Annual Return'].head(rows),})

nest_egg = npf.npv((return_rate-inflation_rate)/100, df.loc[working_years:working_years+retirement_years, 'Goal income num'])
annual_payment = npf.pmt((return_rate-inflation_rate)/100, working_years, 
                            currently_saved, -nest_egg)
monthly_payment = annual_payment/12

#Adding some additional columns that are dependent on previous columns and/or calculations
df['Annual savings num'] = [round(annual_payment)] * rows
df['Annual savings'] = df['Annual savings num'].apply(lambda x: "${:,}".format(x))
df['Goal income'] = df['Goal income num'].apply(lambda x: "${:,}".format(x))
df['Account balance'] = df['Annual savings num'].cumsum() * (1+ df['S&P500 Historical Returns'])


df['asdf'] = df['Annual savings num'].cumsum() 
df['sdfg'] = df['Goal income num'].shift(-1)



st.write("Your nestegg target is ${:,.2f}".format(nest_egg))
st.write("You will need to save ${:,.2f}".format(annual_payment)+" every year to reach you nestegg goal.")
st.write("This comes out to ${:,.2f}".format(monthly_payment))


#st.write(df)
df_temp = df.copy()
df_temp = df_temp.drop(columns=['Goal income num', 'Annual savings num'])
#df_temp['Savings'] = [annual_payment] * rows
graph = df['Goal income num'].plot()




# select the column you want to plot
#data = df['Goal income num'][working_years:working_years+retirement_years]

# create the plot
#plt.plot(data)
#plt.title('Goal Income over Lifetime')
#plt.xlabel('Years')
#plt.ylabel('Dollars')
#plt.yticks([100_000, 200_000, 300_000, 400_000, 500_000])
#plt.xticks([10, 20, 30, 40, 50])

# display the plot in the Streamlit app
#st.pyplot()

st.write(df_temp)


