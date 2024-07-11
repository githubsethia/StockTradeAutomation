import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta

# List of stock tickers
tickers = ['APOLLOHOSP.NS', 'ADANIPOWER.NS', 'IRCTC.NS', 'ADANIENSOL.NS', 'NMDC.NS', 'INDIANB.NS', 'UNIONBANK.NS', 'COALINDIA.NS',
    'ASIANPAINT.NS', 'SBIN.NS', 'TATAMOTORS.NS']

# List of stock tickers
tickers = [
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
   'ATGL.NS', 'VBL.NS', 'SBICARD.NS', 'ADANIGREEN.NS', 'ADANIENSOL.NS', 'CHOLAFIN.NS', 'SRF.NS', 'SIEMENS.NS',
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

# Function to calculate Renko brick size
def calculate_brick_size(current_price):
    return current_price * 0.01

# Calculate the date range for the last 6 months
end_date = datetime.today()
start_date = end_date - timedelta(days=6*30)  # Approximation of 6 months

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
