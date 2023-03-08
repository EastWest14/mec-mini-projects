import os
import math

import requests
from dotenv import load_dotenv  # if missing this module, simply run `pip install python-dotenv`

load_dotenv()
API_KEY = os.getenv('NASDAQ_API_KEY')

r = requests.get(f'https://data.nasdaq.com/api/v3/datasets/FSE/AFX_X/data.json?&start_date=2017-01-01&end_date=2017-12-31&api_key={API_KEY}')
resp = r.json()

highest_opening_price = 0.0
lowest_opening_price = +math.inf
largest_intraday_change = 0.0
largest_change_between_days = 0.0
prev_closing_price = None
sum_trading_volume = 0.0
number_of_collected_volumes = 0
all_trading_volumes = []
for data_point in resp['dataset_data']['data']:
    opening_price = data_point[1]
    high_price = data_point[2]
    low_price = data_point[3]
    closing_price = data_point[4]
    trading_volume = data_point[6]

    if high_price and low_price:
        diff = abs(high_price - low_price)
        if diff > largest_intraday_change:
        	largest_intraday_change = diff

    if closing_price and prev_closing_price:
    	day_change = abs(closing_price - prev_closing_price)
    	if day_change > largest_change_between_days:
    		largest_change_between_days = day_change
    
    if trading_volume:
    	number_of_collected_volumes += 1
    	sum_trading_volume += trading_volume
    	all_trading_volumes.append(trading_volume)

    prev_closing_price = closing_price
    if not opening_price:
    	continue
    if opening_price > highest_opening_price:
        highest_opening_price = opening_price
    if opening_price < lowest_opening_price:
        lowest_opening_price = opening_price

median_trading_volume = 0.0
all_trading_volumes.sort()
if len(all_trading_volumes) % 2:
    mid_value_index = int(len(all_trading_volumes) / 2)
    median_trading_volume = (all_trading_volumes[mid_value_index - 1] + all_trading_volumes[mid_value_index]) * 0.5
else:
	mid_value_index = int((len(all_trading_volumes) - 1) / 2)
	median_trading_volume = all_trading_volumes[mid_value_index]
print(f'Highest opening price: {highest_opening_price}')
print(f'Lowest opening price: {lowest_opening_price}')
print(f'Largest absolute intraday change: {largest_intraday_change:.2f}')
print(f'Largest absolute change between closing prices: {largest_change_between_days:.2f}')
average_trading_volume = sum_trading_volume / float(number_of_collected_volumes)
print(f'Average trading volume: {average_trading_volume:.1f}')
print(f'Median trading volume: {median_trading_volume:.1f}')