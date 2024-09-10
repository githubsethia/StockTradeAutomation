import pandas as pd
import numpy as np
import yfinance as yf

# List of ETFs to analyze
etfs = [
    'GROWEV.NS', 'MIDCAPETF.NS', 'MON100.NS', 'ALPL30IETF.NS', 'GOLDBEES.NS', 
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
    'SETF10GILT.NS', 'EQUAL50ADD.NS', 'HDFCGROWTH.NS'
]

# Create a DataFrame to store crossover results
crossover_results = pd.DataFrame()

# Loop through each ETF to fetch data and analyze
for etf in etfs:
    try:
        # Fetch historical price data, using a maximum period for availability
        df = yf.download(etf, period='3mo')
        
        # Check if data is empty
        if df.empty:
            print(f"No data found for {etf}")
            continue
        
        # Calculate the 20-day and 50-day EMA
        df['EMA20'] = df['Close'].ewm(span=8, adjust=False).mean()
        df['EMA50'] = df['Close'].ewm(span=20, adjust=False).mean()

        # Identify crossovers
        df['Crossover'] = np.where((df['EMA20'] > df['EMA50']) & 
                                   (df['EMA20'].shift(1) <= df['EMA50'].shift(1)), 
                                   df['Close'], np.nan)

        # Filter for crossover points
        crossover_points = df[['Crossover']].dropna().copy()
        crossover_points['Crossover_Date'] = crossover_points.index
        crossover_points['ETF'] = etf

        # Append results to the main DataFrame
        crossover_results = pd.concat([crossover_results, crossover_points], ignore_index=True)

    except Exception as e:
        print(f"Error processing {etf}: {e}")

# Check if there are any crossover results before renaming and sorting
if not crossover_results.empty:
    # Rename and sort results
    crossover_results.columns = ['Crossover_Price', 'Crossover_Date', 'ETF']
    crossover_results = crossover_results.sort_values(by='Crossover_Date', ascending=False)

    # Display only the first 20 results
    print(crossover_results.head(40).reset_index(drop=True))
else:
    print("No crossover results found for any ETF.")