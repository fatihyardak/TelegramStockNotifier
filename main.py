import requests
import telebot
from datetime import datetime, timedelta

# Telegram Bot Token - get this from @BotFather on Telegram
BOT_TOKEN = ''
# Your Telegram Chat ID - you can get this by messaging @userinfobot on Telegram
CHAT_ID = ''

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# API endpoints for daily data
nvda_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=<API-KEY>'
tsla_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=<API-KEY>'
amzn_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=<API-KEY>'

def calculate_price_change(current_price, previous_price):
    change = float(current_price) - float(previous_price)
    change_percent = (change / float(previous_price)) * 100
    return change, change_percent

def get_stock_data(url, symbol):
    response = requests.get(url)
    data = response.json()
    series = data.get('Time Series (Daily)', {})
    dates = list(series.keys())
    
    message = ""
    if len(dates) >= 2:
        current = series[dates[0]]['4. close']
        yesterday = series[dates[1]]['4. close']
        daily_change, daily_percent = calculate_price_change(current, yesterday)
        
        message += f"\n{symbol} Current Price: ${current}\n"
        message += f"Daily Change: ${daily_change:.2f} ({daily_percent:.2f}%)\n"
        
        if len(dates) >= 5:
            week_ago = series[dates[5]]['4. close']
            week_change, week_percent = calculate_price_change(current, week_ago)
            message += f"Weekly Change: ${week_change:.2f} ({week_percent:.2f}%)\n"
    else:
        message += f"\nInsufficient {symbol} data available\n"
    
    return message

def send_telegram_message(message):
    try:
        bot.send_message(CHAT_ID, message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

def main():
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Prepare message
    full_message = f"Stock Market Update ({current_date})\n"
    
    # Get data for each stock
    stocks = [
        (nvda_url, "NVIDIA"),
        (tsla_url, "Tesla"),
        (amzn_url, "Amazon")
    ]
    
    for url, symbol in stocks:
        full_message += get_stock_data(url, symbol)
    
    # Send Telegram message
    send_telegram_message(full_message)

if __name__ == "__main__":
    main()
