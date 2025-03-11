# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 22:38:56 2025

@author: USER
"""

#Task 2
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch FTSE 100 data andSp500 data
ftse100 = yf.download('^FTSE', period='10y', interval='1d')
sp500 = yf.download('^GSPC', period='10y', interval='1d')
ftse100['Daily Return'] = ftse100['Close'].pct_change() * 100
sp500['Daily Return'] = sp500['Close'].pct_change() * 100

# Create a new DataFrame with aligned data
aligned_data = pd.DataFrame({
'FTSE100_Return': ftse100['Daily Return'],
'SP500_Return': sp500['Daily Return']
}).dropna()

#Plot graph
aligned_data.plot(subplots=True, figsize=(10, 6))
16
plt.xlabel('Date')
plt.ylabel('Daily Returns (%)')
plt.title('FTSE100_Return and SP500_Return')
plt.tight_layout()
plt.show()

#show data frame
print(aligned_data.head())
print(aligned_data.tail())

# Regression analysis model
import statsmodels.api as sm
X = sm.add_constant(aligned_data['SP500_Return'])
y = aligned_data['FTSE100_Return']
model = sm.OLS(y, X).fit()
print(model.summary())

# Assuming our aligned data is in 'aligned_data' DataFrame
# M the COVID-19 period starting from March 2020
aligned_data['COVID_Period'] = 0 # Before COVID-19
aligned_data.loc['2020-03-01':, 'COVID_Period'] = 1 # During COVID-19
# Prepare the independent variables
17
X = aligned_data[['SP500_Return', 'COVID_Period']]
X = sm.add_constant(X) # Adding the constant term for the intercept
# The dependent variable remains the FTSE 100 returns
y = aligned_data['FTSE100_Return']
# Perform the regression with the updated independent variables
model_covid = sm.OLS(y, X).fit()

# Display the summary of the updated regression model
print(model_covid.summary())