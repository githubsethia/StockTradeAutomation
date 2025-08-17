import yfinance as yf
import pandas as pd

def calculate_rsi(data, period=28):
    """Calculate RSI using Exponential Moving Average for gains and losses."""
    delta = data['Close'].diff(1)
    
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    # Calculate the Exponential Moving Average for gains and losses
    avg_gain = gain.ewm(span=period, adjust=False).mean()
    avg_loss = loss.ewm(span=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def fetch_stock_data(ticker):
    """Fetch historical data for a stock and calculate RSI."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="3mo")  # Fetch last 30 days for RSI calculation
        data['RSI'] = calculate_rsi(data)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def get_stock_info(tickers):
    """Fetch data for each stock and collect today's High, Low, Close, and RSI."""
    stock_info_list = []

    for ticker in tickers:
        data = fetch_stock_data(ticker)
        if data is not None and not data.empty:
            try:
                today_data = data.iloc[-1]  # Get the most recent day data
                current_price = today_data['Close']
                today_high = today_data['High']
                today_low = today_data['Low']
                today_rsi = today_data['RSI']
                
                # Append stock information as a dictionary
                stock_info_list.append({
                    'Stock': ticker,
                    'Today High': today_high,
                    'Current Price': current_price,
                    'Today Low': today_low,
                    'RSI': today_rsi
                })
            except Exception as e:
                print(f"Error processing data for {ticker}: {e}")

    # Sort the list by RSI in ascending order
    sorted_stock_info = sorted(stock_info_list, key=lambda x: x['RSI'])
    return sorted_stock_info

def print_stock_info(sorted_stock_info):
    """Print stock data in table format."""
    print(f"{'Stock':<12} {'Today High':<12} {'Current Price':<15} {'Today Low':<12} {'RSI':<6}")
    print("-" * 60)

    for stock in sorted_stock_info:
        print(f"{stock['Stock']:<12} {stock['Today High']:<12.2f} {stock['Current Price']:<15.2f} {stock['Today Low']:<12.2f} {stock['RSI']:<6.2f}")

# Stock tickers to fetch data for
tickers = ['ZEEL.NS', 'TTML.NS', 'BMW.NS', 'BAJAJFINSV.NS', 'NMDC.NS', 'PVSL.NS', 'CHENNPETRO.NS', 
           'AXISBANK.NS', 'SWANENERGY.NS', 'TITAN.NS', 'ADANIPOWER.NS', 'IRTCT.NS', 'MEDPLUS.NS',
           'SBIN.NS', 'FDC.NS', 'EICHERMOT.NS']

# Fetch and sort data by RSI in ascending order
sorted_stock_info = get_stock_info(tickers)

# Print the sorted data in table format
print_stock_info(sorted_stock_info)