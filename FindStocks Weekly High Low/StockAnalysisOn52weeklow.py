import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# List of NSE Nifty 50 stocks
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'TCS.NS', 'KOTAKBANK.NS', 
    'HINDUNILVR.NS', 'HDFC.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'ITC.NS', 'BAJFINANCE.NS', 
    'ASIANPAINT.NS', 'AXISBANK.NS', 'LTI.NS', 'DMART.NS', 'HCLTECH.NS', 'LT.NS', 
    'SUNPHARMA.NS', 'BAJAJFINSV.NS', 'MARUTI.NS', 'ULTRACEMCO.NS', 'NESTLEIND.NS', 
    'WIPRO.NS', 'TITAN.NS', 'HEROMOTOCO.NS', 'DRREDDY.NS', 'M&M.NS', 'ADANIGREEN.NS', 
    'POWERGRID.NS', 'GRASIM.NS', 'NTPC.NS', 'TATASTEEL.NS', 'ONGC.NS', 'ADANIPORTS.NS', 
    'COALINDIA.NS', 'TECHM.NS', 'DIVISLAB.NS', 'SBILIFE.NS', 'BPCL.NS', 'BRITANNIA.NS', 
    'SHREECEM.NS', 'JSWSTEEL.NS', 'CIPLA.NS', 'BAJAJ-AUTO.NS', 'HINDALCO.NS', 'IOC.NS', 
    'INDUSINDBK.NS', 'EICHERMOT.NS', 'UPL.NS'
]

# Define constants
TARGET_PROFIT_PERCENT = 6.0
NUM_SHARES = 100
MAX_STOCKS_AT_ONCE = 4
SIMULATION_PERIOD_DAYS = 365

# Helper function to calculate the 52-week low
def calculate_52_week_low(data):
    return data['Low'].rolling(window=252).min()

# Helper function to fetch stock data
def fetch_stock_data(ticker, period):
    return yf.download(ticker, period=period)

# Main function to simulate trading strategy
def simulate_trading(stock_list):
    total_profit = 0
    stock_profit_details = {}
    today = datetime.today()
    start_date = today - timedelta(days=SIMULATION_PERIOD_DAYS)

    for stock in stock_list:
        stock_data = fetch_stock_data(stock, '1y')
        stock_data['52_week_low'] = calculate_52_week_low(stock_data)
        stock_data = stock_data.dropna()
        
        # Tracking variables
        profit = 0
        trade_details = []
        
        for i in range(1, len(stock_data)):
            if stock_data['Low'].iloc[i-1] == stock_data['52_week_low'].iloc[i-1]:  # Previous day was 52-week low
                buy_price = stock_data['High'].iloc[i-1]
                sell_price_target = buy_price * (1 + TARGET_PROFIT_PERCENT / 100)
                
                for j in range(i, len(stock_data)):
                    if stock_data['High'].iloc[j] >= sell_price_target:
                        sell_price = sell_price_target
                        trade_profit = (sell_price - buy_price) * NUM_SHARES
                        profit += trade_profit
                        trade_details.append((stock_data.index[i-1], 'Buy', buy_price, NUM_SHARES))
                        trade_details.append((stock_data.index[j], 'Sell', sell_price, NUM_SHARES))
                        break
        
        stock_profit_details[stock] = {
            'total_profit': profit,
            'trades': trade_details
        }
        total_profit += profit

    return stock_profit_details, total_profit

# Run the simulation
stock_profit_details, total_profit = simulate_trading(nifty_50_stocks)

# Print the results
for stock, details in stock_profit_details.items():
    print(f"Stock: {stock}")
    print(f"Total Profit: ₹{details['total_profit']:.2f}")
    for trade in details['trades']:
        print(f"  Date: {trade[0].strftime('%Y-%m-%d')}, Action: {trade[1]}, Price: ₹{trade[2]:.2f}, Shares: {trade[3]}")
    print()

print(f"Combined Total Profit: ₹{total_profit:.2f}")
