from telegram import Bot

def send_telegram_alerts(token, chat_id, patterns):
    bot = Bot(token=token)
    for symbol, time, pattern in patterns:
        message = f"Pattern Detected: {pattern}\nSymbol: {symbol}\nDate: {time}"
        bot.send_message(chat_id=chat_id, text=message)