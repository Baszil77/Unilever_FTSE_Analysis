# Unilever_FTSE_Analysis

## Overview
This repository examines:
1. **Unilever & FTSE 100** daily return correlations and COVID-19 impacts.
2. **FTSE 100 & S&P 500** correlations, with dummy variables for COVID-19.

Both analyses use Python, `yfinance`, and linear regression (OLS) models from `statsmodels`.

---

## File Descriptions
- **unilever_analysis.py**  
  - Fetches 10 years of daily data for Unilever (`ULVR.L`) and FTSE 100 (`^FTSE`)  
  - Calculates daily returns, plots them, and performs OLS regressions (with and without a COVID period dummy).  

- **sp500_ftse_analysis.py**  
  - Fetches 10 years of daily data for FTSE 100 (`^FTSE`) and S&P 500 (`^GSPC`)  
  - Calculates daily returns and runs regression to see how S&P returns predict FTSE 100 returns, again testing a COVID dummy.

## Key Insights

**Unilever & FTSE**: Typically correlated, but COVID dummy showed limited statistical significance.

**S&P 500 & FTSE**: Strong positive relationship, dummy variables for COVID not significant under basic OLS.

Suggests markets are intertwined, but global events might require advanced or non-linear methods to fully capture their impact.

---

## Requirements
```bash
pip install yfinance matplotlib numpy pandas statsmodels

