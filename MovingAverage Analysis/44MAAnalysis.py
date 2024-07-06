import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of NIFTY 50 stocks (using their ticker symbols)
nifty50_stocks = [
    "ADANIENT.NS", "ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS",
    "BAJAJFINSV.NS", "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS", "DIVISLAB.NS",
    "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS",
    "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS", "INDUSINDBK.NS", "INFY.NS",
    "ITC.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS", "NESTLEIND.NS",
    "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SBILIFE.NS", "SBIN.NS", "SUNPHARMA.NS",
    "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "ULTRACEMCO.NS",
    "UPL.NS", "WIPRO.NS", "ADANIGREEN.NS", "ADANITRANS.NS", "BANKBARODA.NS"
]

# Parameters
MA_period = 44
profit_target = 0.20  # 20%

# Function to calculate buy/sell signals and profit/loss
def calculate_signals_and_profit(stock):
    data = yf.download(stock, period="1y")
    data['44_MA'] = data['Close'].rolling(window=MA_period).mean()
    data['Buy_Signal'] = (data['Close'] > data['44_MA']) & (data['Close'].shift(1) <= data['44_MA'])
    data['Sell_Signal'] = False  # Initialize the column
    
    data['Position'] = 0  # 1 for holding, 0 for not holding
    data['Buy_Price'] = np.nan

    holding = False
    total_profit_loss = 0

    for i in range(1, len(data)):
        if data['Buy_Signal'].iloc[i] and not holding:
            data['Position'].iloc[i] = 1
            data['Buy_Price'].iloc[i] = data['Close'].iloc[i]
            holding = True
        elif holding:
            data['Position'].iloc[i] = 1
            data['Buy_Price'].iloc[i] = data['Buy_Price'].iloc[i-1]
            if (data['Close'].iloc[i] < data['44_MA'].iloc[i]) or (data['Close'].iloc[i] >= data['Buy_Price'].iloc[i] * (1 + profit_target)):
                data['Sell_Signal'].iloc[i] = True
                total_profit_loss += (data['Close'].iloc[i] - data['Buy_Price'].iloc[i]) / data['Buy_Price'].iloc[i]
                holding = False

    return total_profit_loss

# Calculating total profit/loss for each stock
results = {}
for stock in nifty50_stocks:
    profit_loss = calculate_signals_and_profit(stock)
    results[stock] = profit_loss * 100  # Convert to percentage

# Display results
for stock, profit_loss in results.items():
    print(f"{stock}: {profit_loss:.2f}%")

# Optional: Plot the results
plt.figure(figsize=(14, 7))
plt.bar(results.keys(), results.values())
plt.xlabel('Stocks')
plt.ylabel('Total Profit/Loss (%)')
plt.title('Total Profit/Loss for NIFTY 50 Stocks Over the Past Year')
plt.xticks(rotation=90)
plt.show()
