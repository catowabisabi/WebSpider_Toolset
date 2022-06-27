import requests

r = requests.get('http://www.baidu.com')

# r.text是HTML
content = r.text

# r.encoding  # ISO-8859-1 解決亂碼
r.encoding = 'utf-8'
content = r.text

# URL address
content = r.url

# 返回2進制的數據
content = r.content

# 返回 200 404 503 etc.
content = r.status_code

# 返回 headers
content = r.headers






print (content)