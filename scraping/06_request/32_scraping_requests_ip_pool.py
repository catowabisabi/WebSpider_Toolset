import requests


url = 'http://www.google.com/search?'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/102.0.0.0 Safari/537.36',
}

data = {
    'q' : 'my+ip'
}

proxies = {
    'http' : 'http://120.194.55.139:6969' # 要更改這個IP
}

response = requests.get(url = url, params = data, headers = headers, proxies= proxies)
content = response.text
print(content)

with open('proxy.html', 'w', encoding= 'utf-8') as fp:
    fp.write (content)