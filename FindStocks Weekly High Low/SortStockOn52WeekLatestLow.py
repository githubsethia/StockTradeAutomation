import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def find_latest_52_week_low(stocks):
    results = []

    for stock in stocks:
        try:
            # Fetch historical data for the stock
            data = yf.download(stock, start=datetime.now() - timedelta(days=365), end=datetime.now())

            if data.empty:
                print(f"No data available for {stock}")
                continue
            
            # Find the minimum close price in the last 52 weeks
            latest_52_week_low = data['Close'].min()
            latest_52_week_low_date = data[data['Close'] == latest_52_week_low].index[-1]

            # Store the result in a tuple (date, stock symbol, low price)
            results.append((latest_52_week_low_date, stock, latest_52_week_low))

        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
            print()

    # Sort results based on the date of the latest 52-week low in descending order
    results.sort(reverse=True)

    # Print results in descending order
    print("Latest 52-week lows (Descending order):")
    for result in results:
        low_date, stock_symbol, low_price = result
        print(f"Date: {low_date.date()} | Stock: {stock_symbol} | Low Price: {low_price:.2f}")

# Example usage with NIFTY 50, NXT 50, NIFTY 200, NIFTY MIDCAP 100 symbols
stock_list = [
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

print(len(stock_list))
find_latest_52_week_low(stock_list)
