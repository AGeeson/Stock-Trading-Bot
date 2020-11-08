Alpha Vantage and IG bot

Goal:
To create a bot that pulls information on a particular stock. Information is pulled using alpha vantage. Using information and predictive analysis, the program will buy stock on a demo IG account with the goal of making a profit.

Features:
- Pulls stock data information from last 30 days on a particular stock
- Then updates stock information regularly
- Using information and incorporating tested trade practices, elects when and at what price to buy/sell the stock

Strategy for predicting stock price:
1. Get close for each day
1. Create forecast function -.0471*