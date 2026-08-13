# 🛒 Amazon Price Tracker

An automated Python application that tracks the price of an Amazon product and sends an email notification using SMTP when the price drops below a predefined target price.

## 🚀 Features

* 🛒 Scrapes Amazon product prices
* 💰 Tracks the current product price
* 🎯 Compares the price with a target value
* 📧 Sends automated email alerts using SMTP
* 🌐 Uses HTTP request headers
* ⚡ Automates the process of monitoring product prices

## 🛠️ Built With

* Python
* Requests
* BeautifulSoup
* SMTP
* smtplib

## ⚙️ How It Works

1. Sends a request to the Amazon product page.
2. Uses BeautifulSoup to parse the HTML.
3. Extracts the current product price.
4. Compares the current price with the target price.
5. Sends an email notification when the price is below the target.

## 📂 Project Structure

```text
amazon-price-tracker/
│
├── main.py
├── requirements.txt
└── README.md
```

## 📧 Email Notification

When the product reaches the desired price, the application automatically sends an email notification.

Example:

```text
Subject: 🛒 Price Alert!

The product you are watching is now below your target price.

Current Price: $89.99
Target Price: $100.00
```

## 🧠 What I Learned

* Web scraping with BeautifulSoup
* Making HTTP requests with Python
* Extracting data from HTML
* Working with request headers
* Comparing product prices
* Sending emails with SMTP
* Automating tasks with Python

## 🔮 Future Improvements

* Track multiple products
* Track price history
* Add scheduled price checks
* Store products in a database
* Build a web dashboard
* Add support for multiple online stores
* Create HTML email notifications

## 🎯 Project Goal

The goal of this project was to build an automated price-monitoring system that checks Amazon product prices and notifies the user when a product becomes available at or below their desired price.

## 👨‍💻 Author

**Jones Agbramu**

Built as part of my Python development journey and #100DaysOfCode challenge.
