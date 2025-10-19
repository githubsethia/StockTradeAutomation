import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta

stock_symbols = [
    "FLUOROCHEM.NS", "SUMICHEM.NS", "SBICARD.NS", "MARICO.NS", "TATATECH.NS", "PIIND.NS", "ZOMATO.NS", "PRESTIGE.NS",
    "KPRMILL.NS", "SUPREMEIND.NS", "JSL.NS", "THERMAX.NS", "SUNTV.NS", "BAJFINANCE.NS", "ALKEM.NS", "PIDILITIND.NS",
    "ASIANPAINT.NS", "PHOENIXLTD.NS", "GLAND.NS", "GRINDWELL.NS", "MAXHEALTH.NS", "TORNTPOWER.NS", "COFORGE.NS",
    "CRISIL.NS", "3MINDIA.NS", "BALKRISIND.NS", "ZFCVINDIA.NS", "KPITTECH.NS", "JSWSTEEL.NS", "SUNDRMFAST.NS",
    "ENDURANCE.NS", "ACC.NS", "GLAXO.NS", "LTIM.NS", "JINDALSTEL.NS", "MFSL.NS", "DEVYANI.NS", "AUROPHARMA.NS",
    "GODREJIND.NS", "NYKAA.NS", "NESTLEIND.NS", "ISEC.NS", "VOLTAS.NS", "SOLARINDS.NS", "SUNPHARMA.NS", "KALYANKJIL.NS",
    "JUBLFOOD.NS", "ABBOTINDIA.NS", "PGHH.NS", "DMART.NS", "COLPAL.NS", "DIVISLAB.NS", "HINDUNILVR.NS", "JKCEMENT.NS",
    "AUBANK.NS", "JSWINFRA.NS", "HEROMOTOCO.NS", "BERGEPAINT.NS", "MSUMI.NS", "BAJAJ-AUTO.NS", "DABUR.NS", "BRITANNIA.NS",
    "ICICIGI.NS", "SHRIRAMFIN.NS", "AIAENG.NS", "TVSMOTOR.NS", "SBILIFE.NS", "TATASTEEL.NS", "TECHM.NS", "TCS.NS",
    "DRREDDY.NS", "MARUTI.NS", "HINDALCO.NS", "APOLLOHOSP.NS", "EMAMILTD.NS", "BAJAJFINSV.NS", "HDFCBANK.NS",
    "BHARTIARTL.NS", "HAVELLS.NS", "GODREJPROP.NS", "POLYCAB.NS", "SHREECEM.NS", "ZEEL.NS", "POLICYBZR.NS", "KOTAKBANK.NS",
    "POWERGRID.NS", "AJANTPHARM.NS", "STARHEALTH.NS", "NMDC.NS", "WIPRO.NS", "TITAN.NS", "INDIGO.NS", "TORNTPHARM.NS",
    "INDUSINDBK.NS", "SYNGENE.NS", "UBL.NS", "ICICIPRULI.NS", "LINDEINDIA.NS", "NAUKRI.NS", "LTTS.NS", "TRENT.NS",
    "HONAUT.NS", "ADANIGREEN.NS", "CIPLA.NS", "M&M.NS", "SKFINDIA.NS", "MUTHOOTFIN.NS", "VBL.NS", "JSWENERGY.NS",
    "SIEMENS.NS", "LALPATHLAB.NS", "M&MFIN.NS", "APOLLOTYRE.NS", "ONGC.NS", "YESBANK.NS", "BANKINDIA.NS", "TATAPOWER.NS",
    "AWL.NS", "KAJARIACER.NS", "CHOLAFIN.NS", "EICHERMOT.NS", "ULTRACEMCO.NS", "TATACONSUM.NS", "MPHASIS.NS", "KANSAINER.NS",
    "POONAWALLA.NS", "IRCTC.NS", "LLOYDSME.NS", "AMBUJACEM.NS", "ADANIPOWER.NS", "PERSISTENT.NS", "GODREJCP.NS", "UPL.NS",
    "LAURUSLABS.NS", "ASHOKLEY.NS", "MRF.NS", "MANKIND.NS", "SAIL.NS", "ZYDUSLIFE.NS", "SUZLON.NS", "SJVN.NS", "CGPOWER.NS",
    "UNIONBANK.NS", "COROMANDEL.NS", "LT.NS", "ATUL.NS", "ADANIENT.NS", "VEDL.NS", "UNITDSPR.NS", "KEI.NS", "ESCORTS.NS",
    "LODHA.NS", "MAHABANK.NS", "LICHSGFIN.NS", "INFY.NS", "GUJGASLTD.NS", "LUPIN.NS", "ABFRL.NS", "IPCALAB.NS", "DELHIVERY.NS",
    "PAGEIND.NS", "HDFCLIFE.NS", "ABB.NS", "ADANIPORTS.NS", "BDL.NS", "GRASIM.NS", "COALINDIA.NS", "IDFCFIRSTB.NS",
    "BAYERCROP.NS", "ASTRAL.NS", "RVNL.NS", "ITC.NS", "TATAMOTORS.NS", "CUMMINSIND.NS", "HINDZINC.NS", "APLAPOLLO.NS",
    "RELIANCE.NS", "AXISBANK.NS", "PATANJALI.NS", "HAL.NS", "CARBORUNIV.NS", "TATAELXSI.NS", "TATACOMM.NS", "BSE.NS",
    "BAJAJHLDNG.NS", "CONCOR.NS", "ATGL.NS", "IRFC.NS", "DALBHARAT.NS", "HCLTECH.NS", "NTPC.NS", "TATACHEM.NS",
    "SUNDARMFIN.NS", "INDHOTEL.NS", "DEEPAKNTR.NS", "ICICIBANK.NS", "ADANIENSOL.NS", "BATAINDIA.NS", "NHPC.NS", "JIOFIN.NS",
    "HDFCAMC.NS", "GAIL.NS", "BEL.NS", "OBEROIRLTY.NS", "BPCL.NS", "PFC.NS", "RAMCOCEM.NS", "SONACOMS.NS", "IGL.NS",
    "METROBRAND.NS", "DIXON.NS", "UNOMINDA.NS", "SCHAEFFLER.NS", "BIOCON.NS", "PEL.NS", "TIMKEN.NS", "IOC.NS", "FORTIS.NS",
    "LICI.NS", "LTF.NS", "MOTHERSON.NS", "GICRE.NS", "PNB.NS", "MANYAVAR.NS", "FEDERALBNK.NS", "ABCAPITAL.NS",
    "BANKBARODA.NS", "DLF.NS", "PAYTM.NS", "PETRONET.NS", "HINDPETRO.NS", "FACT.NS", "BHEL.NS", "BANDHANBNK.NS",
    "BHARATFORG.NS", "OFSS.NS", "NIACL.NS", "RECLTD.NS", "MAZDOCK.NS", "BOSCHLTD.NS", "TIINDIA.NS", "OIL.NS", "SBIN.NS",
    "SRF.NS", "CANBK.NS", "INDUSTOWER.NS", "IDBI.NS", "INDIANB.NS", "GMRINFRA.NS", "IDEA.NS"
]

# stock_symbols = [
#     "FLUOROCHEM.NS"]

tickers = [symbol.strip() for symbol in stock_symbols]
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
    data = yf.download(ticker, start=start_date, end=end_date, progress=True,auto_adjust=True,multi_level_index=False)
    
    # Ensure the DataFrame has no missing values
    if data is None or data.empty:
        print(f"{ticker}: No data was available")
        continue

    data.dropna(inplace=True)
    
    # Calculate the traditional Renko brick size (1% of the current stock price)
    current_price = data['Close'][-1]
    brick_size = calculate_brick_size(current_price)
    
    # Plot Renko chart using mplfinance's built-in functionality
    renko_params = dict(brick_size=brick_size)
    mpf.plot(data, type='renko', renko_params=renko_params, style='charles', title=ticker)
