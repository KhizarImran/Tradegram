import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

def fetch_mt5_data(symbols, days=7, filepath="data/fx_data.csv"):
    # Initialize MT5 connection
    if not mt5.initialize():
        print("MT5 initialization failed")
        return
    
    # Date range for historical data
    end_time = datetime.now()
    start_time = end_time - timedelta(days=days)

    all_data = []
    for symbol in symbols:
        # Get historical data
        rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_D1, start_time, end_time)
        if rates is not None:
            # Convert to DataFrame
            df = pd.DataFrame(rates)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df['symbol'] = symbol
            all_data.append(df)
    
    # Combine data for all symbols
    if all_data:
        result = pd.concat(all_data, ignore_index=True)
        result.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    else:
        print("No data fetched.")
    
    mt5.shutdown()

# Example usage
if __name__ == "__main__":
    broker_symbols = mt5.symbols_get()  # Fetch all broker symbols
    symbols = [s.name for s in broker_symbols if s.currency_base == "USD"]  # Filter for FX pairs
    fetch_mt5_data(symbols)
