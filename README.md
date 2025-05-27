# StockPulse-Alert-System

StockPulse is a real-time stock monitoring and alert system that notifies users via SMS and WhatsApp about significant changes in stock prices along with the latest news headlines. Built using Flask, Twilio API, Alpha Vantage, and NewsAPI, the system offers an intuitive web interface for users to subscribe to stock alerts instantly.

# 📊 Features

✉️ Sends SMS and WhatsApp alerts for subscribed stocks.

📉 Detects significant price movements (≥1%) using Alpha Vantage data.

🔍 Fetches latest related news using NewsAPI.

🛍️ Simple and responsive web interface built with Flask.

🕛 Scheduled alerts using subprocess automation.

📃 Manages subscribers using JSON-based storage.

# 📥Installation
```bash
# Clone the repository
git clone https://github.com/AaryaButolia11/StockPulse-Alert-System.git
cd StockPulse-Alert-System

# Create a virtual environment and activate
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your credentials
cp .env.example .env
```


