from msilib.schema import TextStyle
import requests
from bs4 import BeautifulSoup as bs
import datetime
from requests.exceptions import ConnectionError as ce
import pandas as pd
import os


def web_content_div(web_content, class_path, value):
    web_content_div = web_content.find_all('div', {'class': class_path})

    try:
        if value != 'None':
            spans = web_content_div[0].find_all(value)
            texts = [span.get_text() for span in spans]
        else:
            texts = []
    except IndexError:
        texts = []

    return texts


def real_time_price(stock_code):
    Error = 0
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'} # Google ',y user agent' to get this line
    url = f'https://finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=finsrch'

    try:
        returnedResponse = requests.get(url)
        web_content = bs(returnedResponse.text,'lxml')


        texts = web_content_div(web_content, 'D(ib) Mend(20px)', 'fin-streamer')
        print(texts)

        price, change, volume, latest_pattern, one_year_target = [], [], [], [], []

        if texts != []:
            price, change = texts[0], texts[1] + ' ' + texts[2]
        else:
            Error = 1
            price, change = [], []

        print (price, change)

        


    except (ce):
        price, change, volume, latest_pattern, one_year_target = [], [], [], [], []
        Error = 1
        print ('Connection Error')


    return price, change, volume, latest_pattern, one_year_target, Error

Stocks = ['ES=F', 'AAPL']

for stock_code in Stocks:
    stock_price, change, volume, latest_pattern, one_year_target, Error = real_time_price(stock_code)
