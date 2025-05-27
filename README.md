# StockPulse-Alert-System

StockPulse is a real-time stock monitoring and alert system that notifies users via SMS and WhatsApp about significant changes in stock prices along with the latest news headlines. Built using Flask, Twilio API, Alpha Vantage, and NewsAPI, the system offers an intuitive web interface for users to subscribe to stock alerts instantly.

# 📊 Features

✉️ Sends SMS and WhatsApp alerts for subscribed stocks.

📉 Detects significant price movements (≥1%) using Alpha Vantage data.

🔍 Fetches latest related news using NewsAPI.

🛍️ Simple and responsive web interface built with Flask.

🕛 Scheduled alerts using subprocess automation.

📃 Manages subscribers using JSON-based storage.


# 📸 ScreenShots
## First Interface
![image](https://github.com/user-attachments/assets/9f616da2-6caf-4120-b72e-348ed6b5f583)

## On entering data
![WhatsApp Image 2025-05-28 at 01 41 28_a413a3c8](https://github.com/user-attachments/assets/0589086e-45bb-456e-bf4a-866419527d98)

## Confirmation Message!
![WhatsApp Image 2025-05-28 at 01 38 49_3b96c69f](https://github.com/user-attachments/assets/0c8311ec-950f-4c8e-ac0d-0800ca73d7c1)


## Message Received!!
![WhatsApp Image 2025-05-28 at 01 49 27_9daf5038](https://github.com/user-attachments/assets/392cd8ad-4db7-47ad-8401-f3960bf1979c)



# 🧰 Tech Stack
Frontend: HTML, Bootstrap (via Jinja2 templates in Flask)

Backend: Python, Flask

APIs:

Alpha Vantage – for real-time stock data

NewsAPI – for fetching news articles

Twilio – for sending SMS and WhatsApp notifications

Data Storage: JSON file-based subscription list

Environment Management: python-dotenv

Process Handling: subprocess.Popen to simulate scheduling


# 📁 Project Structure

StockPulse-Alert-System/<br>
├── static/<br>
│   └── styles.css<br>
├── templates/<br>
│   └── index.html<br>
├── app.py<br>
├── scheduler.py<br>
└── README.md<br>


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

# 🔎 Environment Variables (.env)
```bash
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
STOCK_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_news_api_key
STOCK_ENDPOINT=https://www.alphavantage.co/query
NEWS_ENDPOINT=https://newsapi.org/v2/everything

```

# 🌐 Web Interface

Users can subscribe to a stock alert by entering the stock symbol and phone number.
![image](https://github.com/user-attachments/assets/9f616da2-6caf-4120-b72e-348ed6b5f583)


# 📢 Alert Sample

SMS/WhatsApp messages will look like:

```bash
TSLA: 🔺2%
Headline: Tesla delivers record EV sales in Q2
Brief: Tesla reported record-breaking deliveries...
```

# 🔄 System Workflow

User Interface: Flask app receives stock symbol and phone number.

Background Process: scheduler.py is triggered via subprocess.Popen().

Stock Data: Alpha Vantage API provides daily price updates.

Change Detection: Price difference is calculated and checked.

News Fetching: NewsAPI provides relevant headlines if change ≥1%.

Alert Delivery: Twilio sends SMS and WhatsApp messages.

Logging & Feedback: Console logs and flash messages confirm execution.

# 🔍 Sample Subscription JSON
```bash
{
  "subscriptions": [
    {
      "stock": "AAPL",
      "phone": "+91XXXXXXXXXX"
    }
  ]
}
```

# ✨ Future Enhancements

⌚ Schedule cron jobs for daily automated runs.

🔄 Add email notifications.

💰 Add support for crypto prices.

🌍 User dashboard for managing multiple subscriptions.

🪄 Integrate charts and price history visualization.

💡 Add AI-based news sentiment analysis.


# 📄 License

This project is licensed under the MIT License.

# 🚀 Author
**Aarya Butolia**  
🔗 [GitHub](https://github.com/AaryaButolia11)


Feel free to fork, improve, and contribute to this repository!
