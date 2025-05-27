import sys
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")


def send_alert(stock, phone):
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    data = response.json().get("Time Series (Daily)")

    if not data:
        print(f"Data not found for {stock}")
        return

    data_list = list(data.values())
    y_close = float(data_list[0]["4. close"])
    prev_close = float(data_list[1]["4. close"])
    diff = y_close - prev_close
    up_down = "🔺" if diff > 0 else "🔻"
    diff_percent = round((diff / y_close) * 100)

    if abs(diff_percent) >= 1:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": stock,
        }

        news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
        articles = news_response.json().get("articles", [])[:3]

        formatted_articles = [
            f"{stock}: {up_down}{diff_percent}%\nHeadline: {a['title']}.\nBrief: {a['description']}"
            for a in articles
        ]

        client = Client(account_sid, auth_token)
        for msg in formatted_articles:
            # Send SMS
            client.messages.create(body=msg, from_="+19785765413", to=phone)
            # Send WhatsApp message
            client.messages.create(body=msg, from_="whatsapp:+14155238886", to=f"whatsapp:{phone}")

        print(f"Messages sent for {stock} to {phone}")
    else:
        print(f"No significant change for {stock}, no alert sent.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scheduler.py <stock> <phone>")
        sys.exit(1)

    stock = sys.argv[1]
    phone = sys.argv[2]

    print(f"Scheduler started for stock: {stock}, phone: {phone}")
    send_alert(stock, phone)
