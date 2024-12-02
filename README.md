# Stock Price Notifier Bot

A Telegram bot that sends daily stock updates (price, daily change, and weekly change) for selected companies like NVIDIA, Tesla, and Amazon using the [Alpha Vantage API](https://www.alphavantage.co/).

## Features

- Fetches daily stock prices and changes for predefined companies.
- Sends formatted updates to a specified Telegram chat.
- Calculates daily and weekly percentage changes for better insights.
- Handles errors gracefully (e.g., API issues or insufficient data).

## Technologies Used

- **Python**: Main programming language.
- **Requests**: For API communication.
- **Telebot (pyTelegramBotAPI)**: To interact with Telegram.
- **Alpha Vantage API**: To fetch stock market data.
- **dotenv**: For secure environment variable management.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/fatihyardak/TelegramStockNotifier.git
cd TelegramStockNotifier


