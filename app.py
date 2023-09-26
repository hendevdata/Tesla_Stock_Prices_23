import yfinance as yf
import pandas as pd
import streamlit as st 

st.write("""
    #Simple Stock Price App
        # Shown are the stock closing price of the Volume of Tesla        
 
          
          
         """)

# Define the variable with the Ticker
tickerSimbol = "TSLA"

# Get the stock data on this ticker
tickerData = yf.Ticker(tickerSimbol)

# Get the stock data using a dataframe and the method .history 

tickerDF = tickerData.history(period= '1d', start = '2019-01-01', end = '2023-01-01')


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
