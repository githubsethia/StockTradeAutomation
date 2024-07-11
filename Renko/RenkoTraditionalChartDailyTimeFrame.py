import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Load historical data using yfinance
ticker = "BANKBEES.NS"  # SBI Card ticker on NSE
start_date = "2024-01-01"
end_date = "2024-12-31"

data = yf.download(ticker, start=start_date, end=end_date)['Close']

# Renko chart creation
def create_renko(data, box_size):
    renko = []
    for price in data:
        if not renko:
            renko.append(price)
        else:
            move = price - renko[-1]
            if abs(move) >= box_size:
                steps = int(abs(move) / box_size)
                for _ in range(steps):
                    if move > 0:
                        renko.append(renko[-1] + box_size)
                    else:
                        renko.append(renko[-1] - box_size)
    return renko

# Trading strategy
def trading_strategy(renko):
    positions = []
    position = None
    
    for i in range(2, len(renko)):
        if renko[i] > renko[i-1] and renko[i-1] > renko[i-2]:
            position = renko[i]
            positions.append(('buy', position))
        elif renko[i] < renko[i-1] and position is not None:
            positions.append(('sell', renko[i]))
            position = None
    
    return positions

# Calculate return
def calculate_return(positions):
    returns = 0
    for i in range(0, len(positions), 2):
        if i + 1 < len(positions):
            buy_price = positions[i][1]
            sell_price = positions[i + 1][1]
            returns += (sell_price - buy_price) / buy_price
    return returns

# Set box size
box_size = 10

# Create Renko chart
renko = create_renko(data, box_size)

# Apply trading strategy
positions = trading_strategy(renko)

# Calculate total return
total_return = calculate_return(positions)

# Output the results
print(f"Total Return: {total_return * 100:.2f}%")

# Plot the Renko chart
# plt.figure(figsize=(10, 5))
# plt.plot(data.index, data, label='SBICARD Close Price')
# plt.title('SBICARD Renko Chart')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()
