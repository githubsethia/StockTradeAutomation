import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta

# List of stock tickers
tickers = ['APOLLOHOSP.NS', 'ADANIPOWER.NS', 'IRCTC.NS', 'ADANIENSOL.NS', 'NMDC.NS', 'INDIANB.NS', 'UNIONBANK.NS', 'COALINDIA.NS',
    'ASIANPAINT.NS', 'SBIN.NS', 'TATAMOTORS.NS']

# Function to calculate Renko brick size
def calculate_brick_size(current_price):
    return current_price * 0.01

# Calculate the date range for the last 6 months
end_date = datetime.today()
start_date = end_date - timedelta(days=12*30)  # Approximation of 6 months

print(len(tickers))

# Fetch historical data and plot Renko chart for each stock
for ticker in tickers:
    # Fetch historical stock data
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    # Ensure the DataFrame has no missing values
    data.dropna(inplace=True)
    
    # Calculate the traditional Renko brick size (1% of the current stock price)
    current_price = data['Close'][-1]
    brick_size = calculate_brick_size(current_price)
    
    # Plot Renko chart using mplfinance's built-in functionality
    renko_params = dict(brick_size=brick_size)
    mpf.plot(data, type='renko', renko_params=renko_params, style='charles', title=ticker)
