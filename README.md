# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a simplified Python trading bot for **Binance USDT-M Futures Testnet**.  
It allows placing different types of orders from the command line with proper:

- Input validation  
- Logging  
- Error handling  
- Clean and reusable code structure  

### Supported Order Types
- Market  
- Limit  
- Stop-Limit (Bonus feature)

---

## Project Structure

trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ ├── logging_config.py # Logging setup
│
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
└── trading_bot.log # Generated after running orders



---

## Prerequisites

- Python 3.8 or higher  
- Binance Futures Testnet account  
- Binance Futures Testnet API Key and Secret  

Register for testnet here:  
https://testnet.binancefuture.com  

Important:  
API keys must be generated from Binance Futures Testnet, not from main Binance.

---

## Setup

### 1. Clone the repository
```bash
git clone <https://github.com/abkavi9924/newproj>
cd trading_bot
```


### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate    # Linux / Mac
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
#### In the project root directory, create a file named .env and add:
```bash
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## Usage

### Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 50000
```

### Stop-Limit Order (Bonus)
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.002 --price 50000 --stop_price 49500
```
### Example Output
#### Order Request Summary:
```bash
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}

Order Response:
Order ID: 12345678
Status: FILLED
Executed Qty: 0.002
Avg Price: 49875.2
SUCCESS
```
### Logging

#### All API requests, responses, and errors are logged in:

trading_bot.log


### Example log:
```bash
2026-02-17 18:04:00,598 - INFO - Request: BTCUSDT BUY MARKET 0.002
2026-02-17 18:04:01,012 - INFO - Response: {...}
```

### Log files are required for submission:

#### One Market order

#### One Limit order

#### Validation & Error Handling

### Input validation includes:

#### Order side must be BUY or SELL

#### Order type must be MARKET, LIMIT, or STOP_LIMIT

#### Quantity must be greater than zero

#### Price is required for LIMIT and STOP_LIMIT

#### Stop price is required for STOP_LIMIT

### Handled errors:

#### Invalid user input

#### inance API errors

#### Network or connection failures

### Assumptions

#### Uses Binance USDT-M Futures Testnet

#### Only basic order placement (no leverage or margin configuration)

#### Symbols like BTCUSDT and ETHUSDT are available

#### Minimum order notional is enforced by Binance (>= 100 USDT)

### Bonus Feature Implemented

#### Stop-Limit order support

####Modular project structure

####CLI-based interaction

####Structured logging
