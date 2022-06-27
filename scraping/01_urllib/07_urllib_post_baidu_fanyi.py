import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

#-------------------------
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
#-------------------------

data =  {
    'kw':'kiss'
}

# post 請求的參數 必須要進行編碼
data = urllib.parse.urlencode(data).encode('utf-8') # post的請求的參數必需再編碼
#print(data)

# custom request object 把headers 帶入custom request 
# post的請求是不會放在URL後邊
custom_request = urllib.request.Request(url = url, data = data, headers = headers)
#print(custom_request)


# 發送請求
response = urllib.request.urlopen(custom_request)
#print (response)

content = response.read().decode('utf-8')
#print (content)


import json

json_obj = json.loads(content)
print(json_obj)