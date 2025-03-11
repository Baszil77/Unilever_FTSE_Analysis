# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 22:28:02 2025

@author: USER
"""

APPENDIX

#Task 1
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch historical data for Unilever PLC and FTSE 100 index
unilever = yf.download('ULVR.L', period='10y', interval='1d')
ftse100 = yf.download('^FTSE', period='10y', interval='1d')

# closing prices
unilever['Daily Return'] = unilever['Close'].pct_change() * 100
ftse100['Daily Return'] = ftse100['Close'].pct_change() * 100

# Align the datasets by dates
aligned_data = unilever[['Daily Return']].join(ftse100[['Daily Return']], lsuffix='_unilever', rsuffix='_ftse100', how='inner').dropna()
#show data frame
print(aligned_data.head())
print(aligned_data.tail())
14

#plot graph
aligned_data.plot(subplots=True, figsize=(10, 6))
plt.xlabel('Date')
plt.ylabel('Daily Returns (%)')
plt.title('Unilever and FTSE 100 Daily Returns')
plt.tight_layout()
plt.show()

# First regression
import statsmodels.api as sm
X = sm.add_constant(aligned_data['Daily Return_ftse100']) # Independent variable (FTSE 100 returns)
y = aligned_data['Daily Return_unilever'] # Dependent variable (Unilever returns)
model = sm.OLS(y, X).fit()
print(model.summary())

# Assuming aligned_data is the DataFrame I prepared previously
aligned_data['COVID Period'] = 0 # Default to 0
aligned_data.loc['2020-03-01':, 'COVID Period'] = 1

# Regression analysis
X = aligned_data[['Daily Return_ftse100', 'COVID Period']] # FTSE 100 returns and COVID Period as independent variables
X = sm.add_constant(X) # constant for the intercept
15
y = aligned_data['Daily Return_unilever'] # Dependent variable
model_with_covid = sm.OLS(y, X).fit()
print(model_with_covid.summary())


