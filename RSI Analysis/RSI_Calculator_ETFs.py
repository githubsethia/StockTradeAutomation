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
stock_symbols = [    'GROWEV.NS', 'MIDCAPETF.NS', 'MON100.NS', 'ALPL30IETF.NS', 'GOLDBEES.NS', 
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

# Fetch stock data and calculate RSI
stock_info = fetch_stock_data(stock_symbols)

# Print the fetched stock information in tabular format, sorted by RSI
print_stock_info(stock_info)
