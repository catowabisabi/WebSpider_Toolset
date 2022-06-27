import urllib.request

url1 = 'https://hk-garden.com/forum/' # 403
url2 = 'http://www.google.com' # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 10581: invalid continuation byte
url3 = 'http://www.baidu.com'

response = urllib.request.urlopen(url3)

content = response.read()
content_decoded = content.decode("utf-8")

print(content_decoded)