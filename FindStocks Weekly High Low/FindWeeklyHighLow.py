import pandas as pd
import yfinance as yf

# List of ticker symbols
tickers = ["SBICARD.NS", "ZEEL.NS", "HDFCLIFE.NS", "BERGEPAINT.NS", "TATATECH.NS"]  # Add more ticker symbols as needed

# Dictionary to store weekly high and low prices for each ticker
weekly_data_dict = {}

# Define the date range
start_date = "2024-07-01"
end_date = "2024-07-06"

# Loop through each ticker and process the data
for ticker in tickers:
    # Download historical data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Resample data to weekly frequency, taking the max of the high and min of the low
    weekly_data = data.resample('W').agg({'High': 'max', 'Low': 'min'})
    
    # Store the weekly data in the dictionary
    weekly_data_dict[ticker] = weekly_data
    
    # Display the weekly data for each ticker
    print(f"Weekly data for {ticker}:")
    print(weekly_data)
    print("\n")  # Separator for readability

# Combine all data into a single DataFrame for easy viewing
combined_weekly_data = pd.concat(weekly_data_dict, axis=1)

# Display the combined weekly high and low prices
print("Combined weekly high and low prices for all tickers:")
print(combined_weekly_data)

# Optionally, save to CSV
#combined_weekly_data.to_csv("multiple_stocks_weekly_high_low.csv")
