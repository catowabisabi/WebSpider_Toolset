import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests


url_stats = 'https:finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'F'

#
response = requests.get(url_financials.format(stock, stock))
soup = BeautifulSoup(response.text, 'html.parser')

# find the content with regular expression #js
pattern = re.compile (r'\s--\sData\s--\s')
# return the contents of the elements and and get the first element
script_data = soup.find('script', text=pattern).contents[0]

# beginning
print(script_data[:500])