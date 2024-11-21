# **Tradegram: Automated Candlestick Pattern Scanner**

## **Overview**
Tradegram is a Python-based tool designed to scan the forex market for specific candlestick patterns, such as bullish and bearish engulfing patterns, using data from the MetaTrader 5 (MT5) platform. The identified patterns are then sent as notifications to a Telegram group, enabling manual trading decisions.

---

## **Features**
- Fetches OHLC (Open, High, Low, Close) data for the last 7 days for all forex pairs available in the MT5 terminal.
- Identifies candlestick patterns like **Bullish Engulfing** and **Bearish Engulfing**.
- Sends pattern alerts to a specified Telegram group.
- Automates daily updates with a scheduled job.
- Lightweight and customizable for other candlestick patterns.

---

## **Project Structure**
```plaintext
market_candlestick_scanner/
│
├── data/
│   └── fx_data.csv               # CSV file storing the latest market data
│
├── src/
│   ├── fetch_data_mt5.py         # Script to fetch data from MT5
│   ├── pattern_detector.py       # Script to identify candlestick patterns
│   ├── telegram_notifier.py      # Script to send Telegram messages
│   ├── scheduler.py              # Orchestrates daily automation
│   └── config.py                 # Configuration settings (MT5, Telegram)
│
├── logs/
│   └── app.log                   # Logs execution details
│
├── .gitignore                    # Excludes unnecessary files (e.g., venv/)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── main.py                       # Entry point to run the pipeline