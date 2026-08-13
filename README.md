🛒 Amazon Price Tracker

An automated Python application that monitors the price of an Amazon product and sends an email alert using SMTP when the price drops below a predefined target value.

The project uses BeautifulSoup to scrape the product price from Amazon and Python's SMTP tools to automatically notify the user when the product becomes affordable.

🚀 Features
🛒 Scrapes live Amazon product information
💰 Tracks the current product price
🎯 Compares the price against a predefined target price
📧 Sends an automated email alert using SMTP
🌐 Uses HTTP request headers to access the website
🔄 Can be automated to check prices regularly
🔐 Keeps email credentials and sensitive information out of the source code
🛠️ Built With
Python
Requests
BeautifulSoup
SMTP / smtplib
Environment Variables
⚙️ How It Works
        Amazon Product
              │
              ▼
       Send HTTP Request
              │
              ▼
        BeautifulSoup
              │
              ▼
       Extract Product Price
              │
              ▼
      Compare With Target
          Price
        /         \
      No           Yes
      │             │
      ▼             ▼
   Continue     Send Email
                via SMTP
                    │
                    ▼
               📧 Alert
📂 Project Structure
amazon-price-tracker/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
📦 Installation
1. Clone the repository
git clone https://github.com/yourusername/amazon-price-tracker.git
2. Navigate into the project
cd amazon-price-tracker
3. Install the required packages
pip install -r requirements.txt
4. Configure your environment variables

Create a .env file containing your email credentials and other sensitive information.

Example:

MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password

Important: Never upload your .env file or email credentials to GitHub.

▶️ Running the Project

Run the application with:

python main.py

The program will:

Request the Amazon product page.
Parse the page using BeautifulSoup.
Extract the current product price.
Compare it with the target price.
Send an email notification if the price is low enough.
📧 Email Alerts

When the product price reaches or falls below the target price, the application sends an automated email.

Example:

Subject: 🛒 Price Alert!

The product you are watching is now below your target price.

Current Price: $89.99
Target Price: $100.00

Check the product and grab the deal!
🧠 What I Learned

This project helped me learn how to build a practical web-scraping and automation application using Python.

Web Scraping
Using requests to make HTTP requests
Using BeautifulSoup to parse HTML
Finding specific elements within a webpage
Extracting product information from a live website
Price Tracking
Extracting and converting product prices
Comparing current prices with target prices
Creating automated price-based conditions
Email Automation
Working with SMTP
Sending automated emails with Python
Creating email notifications based on program conditions
Web Requests
Adding request headers
Working with HTTP responses
Handling website requests
Security
Using environment variables
Protecting email credentials
Keeping sensitive information out of GitHub
🔮 Future Improvements

Track multiple Amazon products

Store product price history

Track price changes over time

Add scheduled automatic checks

Add a database for tracked products

Build a web dashboard

Add support for multiple stores

Add HTML-formatted email notifications

🎯 Project Goal

The goal of this project was to build an automated system that removes the need to manually check Amazon for price drops.

Instead of repeatedly visiting a product page, the application checks the price automatically and sends an email notification when the product reaches the desired price.

👨‍💻 Author

Jones Agbramu

Built as part of my Python development journey and #100DaysOfCode challenge.
