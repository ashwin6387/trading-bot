# Binance Futures Trading Bot

A production-style Python CLI trading bot for placing MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).

Built as part of a Python Developer Internship assignment to demonstrate:
- API integration
- clean backend architecture
- CLI development
- logging & monitoring
- exception handling
- reusable Python code structure

---

# Features

## Trading Features
- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- Real-time order execution

## CLI Features
- Command-line based interaction using argparse
- User input validation
- Helpful error messages
- Clean terminal output

## Engineering Features
- Modular project structure
- Separate API/client layer
- Logging support
- Exception handling
- Environment variable security
- Reusable and scalable codebase

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| python-binance | Binance API wrapper |
| argparse | CLI input handling |
| logging | Application logging |
| python-dotenv | Environment variable management |

---

# Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repository_url>
cd trading_bot
```

---

## 2. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Binance Testnet Setup

## 1. Create Binance Futures Testnet Account

Visit:

https://testnet.binancefuture.com

---

## 2. Generate API Keys

Generate:
- API Key
- Secret Key

---

## 3. Create `.env` File

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

# Running the Application

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

# CLI Parameters

| Parameter | Description | Required |
|---|---|---|
| --symbol | Trading pair | Yes |
| --side | BUY or SELL | Yes |
| --type | MARKET or LIMIT | Yes |
| --quantity | Order quantity | Yes |
| --price | Required for LIMIT orders | LIMIT only |

---

# Sample Output

## Successful MARKET Order

```bash
==================================
Order Request Summary
==================================
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

==================================
Order Executed Successfully
==================================
Order ID    : 123456789
Status      : FILLED
ExecutedQty : 0.001
```

---

# Logging

Application logs are stored in:

```bash
logs/trading.log
```

The log file records:
- API requests
- API responses
- order execution details
- validation failures
- exception/error details

---

# Validation & Error Handling

The application handles:
- Invalid symbols
- Invalid order types
- Invalid quantity values
- Missing LIMIT order price
- Binance API exceptions
- Network failures
- Unexpected runtime exceptions

---

# Security

Sensitive credentials are stored securely using environment variables.

`.env` file is excluded from Git tracking using:

```gitignore
.env
```

---

# Assumptions

- Application is designed only for Binance Futures Testnet
- Only USDT-M Futures contracts are supported
- LIMIT orders use GTC (Good Till Cancelled)
- User already has Binance Testnet API credentials

---

# Future Improvements

Possible future enhancements:
- Stop-Limit Orders
- OCO Orders
- Web Dashboard
- Database storage
- Docker support
- Unit testing
- Async order execution
- Telegram/Discord notifications

---

# How This Project Demonstrates Backend Skills

This project demonstrates:
- REST/API integration
- Modular Python architecture
- CLI application development
- Logging and debugging
- Error handling best practices
- Environment management
- Clean code principles

---

# Author

Ashwin Vishwakarma

Python Developer | DevOps Enthusiast

---

# License

This project is created for educational and assessment purposes only.
