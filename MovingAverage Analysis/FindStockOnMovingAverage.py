import pandas as pd
import yfinance as yf

# Define the Nifty 50 stock symbols
nifty_50_symbols = [
    'DRREDDY.NS', 'ONGC.NS', 'RELIANCE.NS', 'HEROMOTOCO.NS', 'SBILIFE.NS', 'TATAMOTORS.NS', 'DIVISLAB.NS', 'COALINDIA.NS',
    'ASIANPAINT.NS', 'GRASIM.NS', 'TATACONSUM.NS', 'HINDALCO.NS', 'BAJAJ-AUTO.NS', 'TITAN.NS', 'NESTLEIND.NS', 'NTPC.NS',
    'WIPRO.NS', 'SBIN.NS', 'BRITANNIA.NS', 'HCLTECH.NS', 'TATASTEEL.NS', 'HDFCLIFE.NS', 'SUNPHARMA.NS', 'HINDUNILVR.NS',
    'CIPLA.NS', 'LT.NS', 'ADANIENT.NS', 'APOLLOHOSP.NS', 'POWERGRID.NS', 'ITC.NS', 'TECHM.NS', 'INFY.NS', 'BPCL.NS',
    'ULTRACEMCO.NS', 'HDFCBANK.NS', 'BAJFINANCE.NS', 'TCS.NS', 'ADANIPORTS.NS', 'BAJAJFINSV.NS', 'M&M.NS', 'JSWSTEEL.NS',
    'EICHERMOT.NS', 'SHRIRAMFIN.NS', 'MARUTI.NS', 'INDUSINDBK.NS', 'KOTAKBANK.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS', 'AXISBANK.NS',
    'PNB.NS', 'TRENT.NS', 'VEDL.NS', 'ZYDUSLIFE.NS', 'BEL.NS', 'JIOFIN.NS', 'CANBK.NS', 'RECLTD.NS', 'AMBUJACEM.NS', 'IOC.NS',
    'PFC.NS', 'BANKBARODA.NS', 'ICICIPRULI.NS', 'NAUKRI.NS', 'GAIL.NS', 'GODREJCP.NS', 'BAJAJHLDNG.NS', 'DLF.NS', 'TVSMOTOR.NS',
    'TORNTPHARM.NS', 'BERGEPAINT.NS', 'PIDILITIND.NS', 'MARICO.NS', 'IRFC.NS', 'TATAPOWER.NS', 'INDIGO.NS', 'ICICIGI.NS',
    'ADANIPOWER.NS', 'SHREECEM.NS', 'DABUR.NS', 'LICI.NS', 'IRCTC.NS', 'ZOMATO.NS', 'COLPAL.NS', 'HAL.NS', 'JINDALSTEL.NS',
    'UNITDSPR.NS', 'ATGL.NS', 'VBL.NS', 'SBICARD.NS', 'ADANIGREEN.NS', 'ADANIENSOL.NS', 'CHOLAFIN.NS', 'SRF.NS', 'SIEMENS.NS',
    'ABB.NS', 'HAVELLS.NS', 'BOSCHLTD.NS', 'MOTHERSON.NS', 'DMART.NS', 'TATAMTRDVR.NS', 'LTIM.NS', 'PERSISTENT.NS', 'SAIL.NS',
    'MRF.NS', 'PETRONET.NS', 'INDUSTOWER.NS', 'GODREJPROP.NS', 'LUPIN.NS', 'MAXHEALTH.NS', 'JUBLFOOD.NS', 'BANDHANBNK.NS',
    'DIXON.NS', 'AUROPHARMA.NS', 'BHEL.NS', 'ALKEM.NS', 'DALBHARAT.NS', 'LTF.NS', 'ABCAPITAL.NS', 'YESBANK.NS', 'TIINDIA.NS',
    'BALKRISIND.NS', 'MPHASIS.NS', 'AUBANK.NS', 'NMDC.NS', 'UPL.NS', 'FEDERALBNK.NS', 'OBEROIRLTY.NS', 'OFSS.NS', 'ESCORTS.NS',
    'LTTS.NS', 'GUJGASLTD.NS', 'IDFCFIRSTB.NS', 'M&MFIN.NS', 'TATACOMM.NS', 'ASHOKLEY.NS', 'INDHOTEL.NS', 'HINDPETRO.NS',
    'MFSL.NS', 'PIIND.NS', 'COFORGE.NS', 'CONCOR.NS', 'BHARATFORG.NS', 'ACC.NS', 'SUZLON.NS', 'HDFCAMC.NS', 'ASTRAL.NS',
    'PAGEIND.NS', 'GMRINFRA.NS', 'IDEA.NS', 'CUMMINSIND.NS', 'POLYCAB.NS', 'KALYANKJIL.NS', 'PATANJALI.NS', 'APOLLOTYRE.NS',
    'KPITTECH.NS', 'IGL.NS', 'IPCALAB.NS', 'JSWINFRA.NS', 'SUPREMEIND.NS', 'OIL.NS', 'FACT.NS', 'NHPC.NS', 'PRESTIGE.NS',
    'BIOCON.NS', 'LALPATHLAB.NS', 'APLAPOLLO.NS', 'LICHSGFIN.NS', 'TATACHEM.NS', 'PEL.NS', 'BSE.NS', 'IDBI.NS', 'CGPOWER.NS',
    'POONAWALLA.NS', 'POLICYBZR.NS', 'RVNL.NS', 'INDIANB.NS', 'TATATECH.NS', 'GLAND.NS', 'LAURUSLABS.NS', 'ZEEL.NS', 'TATAELXSI.NS',
    'DELHIVERY.NS', 'SYNGENE.NS', 'BANKINDIA.NS', 'SUNTV.NS', 'NYKAA.NS', 'BDL.NS', 'DEEPAKNTR.NS', 'MANKIND.NS', 'MAHABANK.NS',
    'JSWENERGY.NS', 'PAYTM.NS', 'SJVN.NS', 'FORTIS.NS', 'SONACOMS.NS', 'UNIONBANK.NS', 'TORNTPOWER.NS', 'VOLTAS.NS', 'ABFRL.NS',
    'LODHA.NS', 'MAZDOCK.NS', 'IDEA.NS', 'CUMMINSIND.NS', 'POLYCAB.NS', 'MOTHERSON.NS', 'DMART.NS'
]

# nifty_50_symbols = [
#     "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
#     "HINDUNILVR.NS", "SBIN.NS", "KOTAKBANK.NS", "BAJFINANCE.NS", "BHARTIARTL.NS",
#     "ITC.NS", "HDFC.NS", "ASIANPAINT.NS", "HCLTECH.NS", "MARUTI.NS",
#     "LT.NS", "AXISBANK.NS", "ULTRACEMCO.NS", "SUNPHARMA.NS", "WIPRO.NS",
#     "NESTLEIND.NS", "ADANIGREEN.NS", "JSWSTEEL.NS", "TITAN.NS", "TECHM.NS",
#     "POWERGRID.NS", "ONGC.NS", "INDUSINDBK.NS", "M&M.NS", "BAJAJFINSV.NS",
#     "TATASTEEL.NS", "NTPC.NS", "DIVISLAB.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS",
#     "COALINDIA.NS", "BPCL.NS", "EICHERMOT.NS", "BRITANNIA.NS", "GRASIM.NS",
#     "DRREDDY.NS", "TATAMOTORS.NS", "CIPLA.NS", "UPL.NS", "ADANIPORTS.NS",
#     "SBILIFE.NS", "SHREECEM.NS", "IOC.NS", "APOLLOHOSP.NS", "BAJAJ-AUTO.NS"
# ]

# Function to fetch historical data for a stock
def fetch_data(symbol, period="1mo"):
    return yf.download(symbol, period=period)

# Function to calculate moving averages
def calculate_moving_averages(df, short_window=5, long_window=8):
    df[f"SMA_{short_window}"] = df['Close'].rolling(window=short_window).mean()
    df[f"SMA_{long_window}"] = df['Close'].rolling(window=long_window).mean()
    return df

# Function to find buy and sell signals
def find_signals(df, short_window=5, long_window=8):
    if len(df) < long_window:
        return None, None

    signals = []

    for i in range(-3, 0):
        if i == -1:
            yesterday = df.index[i]
            day_before_yesterday = df.index[i - 1]

            buy_signal = (df[f"SMA_{short_window}"].loc[yesterday] > df[f"SMA_{long_window}"].loc[yesterday] and
                          df[f"SMA_{short_window}"].loc[day_before_yesterday] <= df[f"SMA_{long_window}"].loc[day_before_yesterday])

            sell_signal = (df[f"SMA_{short_window}"].loc[yesterday] < df[f"SMA_{long_window}"].loc[yesterday] and
                           df[f"SMA_{short_window}"].loc[day_before_yesterday] >= df[f"SMA_{long_window}"].loc[day_before_yesterday])
        else:
            yesterday = df.index[i]
            buy_signal = sell_signal = False

        signals.append((yesterday, df['Close'].loc[yesterday], buy_signal, sell_signal))

    return signals

# Main function to analyze Nifty 50 stocks
def analyze_stocks(symbols):
    buy_signals = []
    sell_signals = []

    for symbol in symbols:
        df = fetch_data(symbol)
        df = calculate_moving_averages(df)

        signals = find_signals(df)
        for signal in signals:
            date, close_price, buy_signal, sell_signal = signal
            if buy_signal:
                buy_signals.append((symbol, date, close_price, 'Buy'))
            if sell_signal:
                sell_signals.append((symbol, date, close_price, 'Sell'))

    return buy_signals, sell_signals

# Analyze Nifty 50 stocks
buy_signals, sell_signals = analyze_stocks(nifty_50_symbols)

# Combine and sort signals
all_signals = buy_signals + sell_signals
all_signals.sort(key=lambda x: x[1], reverse=True)

# Print the results
print(f"{'Stock':<15} {'Date':<12} {'Close Price':<12} {'Signal':<5}")
for signal in all_signals:
    stock, date, close_price, signal_type = signal
    print(f"{stock:<15} {date.strftime('%Y-%m-%d'):<12} {close_price:<12.2f} {signal_type:<5}")
