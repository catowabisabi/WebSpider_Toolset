from bs4 import BeautifulSoup as bs

soup = bs(response.read().decode, 'lxml')