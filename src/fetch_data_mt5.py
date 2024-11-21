import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

# Initialize MT5
if not mt5.initialize():
    print("Failed to initialize MT5:", mt5.last_error())
    quit()

# Ensure we are connected to the account
account_info = mt5.account_info()
if account_info is None:
    print("Failed to connect to MT5 account:", mt5.last_error())
    mt5.shutdown()
    quit()

print(f"Connected to MT5 account: {account_info.login}")

# Fetch all symbols from the broker
broker_symbols = mt5.symbols_get()
if broker_symbols is None:
    print("Failed to retrieve symbols:", mt5.last_error())
    mt5.shutdown()
    quit()

# Filter USD-based forex pairs
symbols = [s.name for s in broker_symbols if s.currency_base == "USD"]
if not symbols:
    print("No USD-based forex pairs found.")
    mt5.shutdown()
    quit()

print(f"Found {len(symbols)} USD-based forex pairs.")

# Fetch OHLC data for the past 7 days for each symbol
ohlc_data = []

for symbol in symbols:
    # Ensure the symbol is visible in the terminal
    if not mt5.symbol_select(symbol, True):
        print(f"Failed to select symbol: {symbol}")
        continue

    # Fetch data
    utc_from = datetime.now() - timedelta(days=7)
    utc_to = datetime.now()
    rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_D1, utc_from, utc_to)

    if rates is None:
        print(f"Failed to retrieve data for {symbol}")
        continue

    # Convert to a DataFrame
    df = pd.DataFrame(rates)
    df['symbol'] = symbol
    ohlc_data.append(df)

# Combine all data and save to CSV
if ohlc_data:
    result = pd.concat(ohlc_data, ignore_index=True)
    result['time'] = pd.to_datetime(result['time'], unit='s')
    result.to_csv("data/fx_data.csv", index=False)
    print("Data successfully saved to data/fx_data.csv.")
else:
    print("No data retrieved for any symbols.")

# Shutdown MT5
mt5.shutdown()
