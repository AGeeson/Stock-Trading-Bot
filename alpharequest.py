import requests, json
from sklearn.linear_model import LinearRegression
import numpy as np

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"symbol":"HSBC","function":"TIME_SERIES_DAILY", "outputsize":"compact"}

# don't forget to add your alphavantage api key
alphaVantageAPIkey = ""

headers = {
    'x-rapidapi-key': alphaVantageAPIkey,
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

#request to alpha vantage
response = requests.request("GET", url, headers=headers, params=querystring)

#as oppose to live_data, turns alpha vantage response in json
historical_data = response.json()
print("All 'close' data")
#manipulates json for readability and practicality
a = (historical_data['Time Series (Daily)'].values())

# creates numpy arrays for x and y coords
y_closes = []
x_inputs= []
for x in a:
    y_closes.append(float(x['4. close']))
    x_inputs.append(len(y_closes))
print(y_closes)
print(x_inputs)
x = np.array([x_inputs]).reshape(-1,1)
y = np.array(y_closes)

# uses sklearn LinearRegression method to display regression data
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# predicts the next data point, the closing stock price on next trading day
y_pred = model.predict(np.array([101]).reshape(-1,1))
print('Estimate of closing price for ' + querystring["symbol"] + ' stock on the next trading day:', "{:.2f}".format(y_pred[0]), sep='\n')