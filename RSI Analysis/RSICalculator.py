import yfinance as yf
import pandas as pd

def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI) for a given stock data.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def fetch_stock_data(stock_symbols):
    """
    Fetch data for given stock symbols and calculate RSI.
    """
    stock_info = []

    for symbol in stock_symbols:
        # Fetch stock data for the past 30 days
        stock_data = yf.download(symbol, period="1mo", interval="1d")
        
        if not stock_data.empty:
            # Calculate RSI for the stock
            stock_data['RSI'] = calculate_rsi(stock_data)

            # Get today's high, low, and current price (last close price)
            today_high = stock_data['High'].iloc[-1]   # Use .iloc[-1] to access the last row
            today_low = stock_data['Low'].iloc[-1]     # Use .iloc[-1] to access the last row
            current_price = stock_data['Close'].iloc[-1]  # Use .iloc[-1] to access the last row
            rsi_today = stock_data['RSI'].iloc[-1]     # Use .iloc[-1] to access the last row

            # Append the data to the list as a dictionary
            stock_info.append({
                "Stock": symbol,
                "Today High": today_high,
                "Current Price": current_price,
                "Today Low": today_low,
                "RSI": rsi_today
            })
    
    return stock_info

def print_stock_info(stock_info):
    """
    Print the stock information including RSI, High, Current Price, and Low in tabular format,
    sorted by the lowest RSI in ascending order.
    """
    # Convert the stock information to a DataFrame
    df = pd.DataFrame(stock_info)
    # Sort the DataFrame by the 'RSI' column in ascending order
    df_sorted = df.sort_values(by="RSI", ascending=True)
    # Display the sorted DataFrame in a tabular format
    print(df_sorted.to_string(index=False, float_format="%.2f"))

# List of stock symbols to analyze
stock_symbols = ["RKSWAMY.NS", "TTML.NS", "ZEEL.NS", "RALLIS.NS", "M&MFIN.NS", "HAVELLS.NS", "AXISBANK.NS",
                 "SBIN.NS", "ADANIPOWER.NS", "IRCTC.NS", "NMDC.NS", "UNIONBANK.NS", "ASHIANA.NS", "BMW.BS",
                 "BAJAJFINSV.NS", "MEDPLUS.NS", "PVSL.NS", "TITAN.NS", "YATHARTH.NS"]

# Fetch stock data and calculate RSI
stock_info = fetch_stock_data(stock_symbols)

# Print the fetched stock information in tabular format, sorted by RSI
print_stock_info(stock_info)