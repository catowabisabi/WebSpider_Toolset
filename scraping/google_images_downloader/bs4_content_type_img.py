import requests
from bs4 import BeautifulSoup

def get_images_with_request_headers(search_query):
  params = {
      "q": "{}".format(search_query),
      "tbm": "isch", 
      "content-type": "image/png",
  }

  html = requests.get("https://www.google.com/search", params=params)
  soup = BeautifulSoup(html.text, 'html.parser')

  for img in soup.select("img"):
    print(img["src"])