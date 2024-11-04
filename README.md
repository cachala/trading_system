# Django REST API Trading System

A simple Django REST API for a trading system where a user can place orders and view their portfolio value.

## Features
- Place stock orders
- Retrieve portfolio value
- View details of individual stocks

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/cachala/trading-system.git

2. Run migrations:
   ```bash
   python manage.py migrate

3. Start the server:
   ```bash
   python manage.py runserver

## API Endpoints

- /place-order/: Place an order
- /total-value/: Retrieve total portfolio value
- /id/: Get individual stock details
