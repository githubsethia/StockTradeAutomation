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
tickers = ['GROWEV.NS', 'MIDCAPETF.NS', 'MON100.NS', 'ALPL30IETF.NS', 'GOLDBEES.NS', 
    'TATSILV.NS', 'ALPHAETF.NS', 'ALPHA.NS', 'ITIETF.NS', 'SETFGOLD.NS', 
    'BANKBEES.NS', 'MOM30IETF.NS', 'SILVERBEES.NS', 'MIDCAPIETF.NS', 
     'NIFTYETF.NS', 'NIFTYIETF.NS', 'SILVERETF.NS', 'GOLD1.NS', 
    'LOWVOLIETF.NS', 'TNIDETF.NS', 'EVINDIA.NS', 'CPSEETF.NS', 'ITBEES.NS', 
    'PHARMABEES.NS', 'IT.NS', 'LOWVOL1.NS', 'MAFANG.NS', 
     'MOSMALL250.NS', 'FMCGIETF.NS', 'GOLDCASE.NS', 'MID150BEES.NS', 
    'NV20IETF.NS', 'MOM100.NS', 'OILIETF.NS', 'TATAGOLD.NS', 'ABSLPSE.NS', 
    'NIFTYBEES.NS', 'HDFCSML250.NS', 'GILT5YBEES.NS', 'NEXT50IETF.NS', 'AUTOIETF.NS', 
    'HDFCSILVER.NS', 'PSUBNKIETF.NS', 'HEALTHY.NS', 'BFSI.NS', 'HDFCPVTBAN.NS', 
    'BSLNIFTY.NS', 'SETFNIF50.NS', 'HDFCMID150.NS', 'QUAL30IETF.NS', 'GOLDIETF.NS', 
    'LTGILTBEES.NS', 'HDFCGOLD.NS',  'ICICIB22.NS', 'PVTBANIETF.NS', 
    'SILVERIETF.NS', 'PSUBNKBEES.NS', 'SMALLCAP.NS', 'UTIBANKETF.NS', 'MAHKTECH.NS', 
    'MIDSMALL.NS', 'BSE500IETF.NS', 'MOVALUE.NS', 'MIDSELIETF.NS',  
    'MID150CASE.NS', 'ABSLBANETF.NS', 'HDFCMOMENT.NS', 'JUNIORBEES.NS', 'GOLDETFADD.NS', 
    'HDFCNIFIT.NS', 'MONIFTY500.NS', 'ITETF.NS', 'UTINEXT50.NS', 'NIF100IETF.NS', 
    'HDFCNEXT50.NS', 'BANKIETF.NS', 'AUTOBEES.NS', 'COMMOIETF.NS', 'INFRAIETF.NS', 
    'AXISGOLD.NS', 'FINIETF.NS', 'MASPTOP50.NS', 'MONQ50.NS', 'IVZINNIFTY.NS', 
    'MOLOWVOL.NS', 'TECH.NS', 'SILVER.NS', 'NIFTY1.NS', 'MAKEINDIA.NS', 
    'MOREALTY.NS', 'GOLDETF.NS', 'MOMOMENTUM.NS', 'NV20.NS', 'GOLDSHARE.NS', 
    'MOGSEC.NS', 'TOP100CASE.NS', 'QGOLDHALF.NS', 'HDFCPSUBK.NS', 'MOMENTUM.NS', 
    'HDFCBSE500.NS', 'ESILVER.NS',  'BANKETFADD.NS', 'HDFCNIFBAN.NS', 
    'HEALTHIETF.NS', 'BANKBETF.NS', 'HDFCSENSEX.NS', 'AXISBPSETF.NS', 'CONSUMBEES.NS', 
    'PVTBANKADD.NS', 'HNGSNGBEES.NS',  'HDFCNIFTY.NS', 'MIDCAP.NS', 
    'SILVERADD.NS', 'DIVOPPBEES.NS', 'SETFNIFBK.NS', 'SILVER1.NS', 'LICNETFGSC.NS', 
    'MOHEALTH.NS', 'EBBETF0425.NS', 'UTINIFTETF.NS', 'SETFNN50.NS', 'NIFTYQLITY.NS', 
    'BSLGOLDETF.NS', 'SBISILVER.NS', 'HDFCNIF100.NS', 'PSUBANKADD.NS', 
    'BANKNIFTY1.NS',  'ITETFADD.NS', 'SBINEQWETF.NS', 'ESG.NS', 
    'ABSLNN50ET.NS', 'AXISTECETF.NS', 'PSUBANK.NS', 'NV20BEES.NS', 
    'EBBETF0431.NS', 'EBBETF0430.NS', 'AXISILVER.NS', 'SENSEXETF.NS', 'INFRABEES.NS', 
    'SILVRETF.NS', 'HDFCQUAL.NS', 'NIF100BEES.NS', 'CONSUMIETF.NS', 'MNC.NS', 
    'HDFCLOWVOL.NS', 'SBIETFCON.NS', 'SBIETFIT.NS', 'AXISHCETF.NS', 'HDFCVALUE.NS', 
    'SETF10GILT.NS', 'EQUAL50ADD.NS', 'HDFCGROWTH.NS']

# Fetch and sort data by RSI in ascending order
sorted_stock_info = get_stock_info(tickers)

# Print the sorted data in table format
print_stock_info(sorted_stock_info)
