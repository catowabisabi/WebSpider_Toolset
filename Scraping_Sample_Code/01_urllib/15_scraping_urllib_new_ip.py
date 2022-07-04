import urllib.request



# 使用handler 來訪問百度來提取網頁源碼

url = 'https://www.baidu.com/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

request = urllib.request.Request(url = url, headers = headers)

#生産一個代理, 百度快代理
proxies = {
    'http':'202.55.5.209:8090'
}

#使用handler, build_opener, open

# 建立handler
handler = urllib.request.ProxyHandler(proxies)

# 利用handler建立opener
opener = urllib.request.build_opener(handler)

# 使用open功能
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)