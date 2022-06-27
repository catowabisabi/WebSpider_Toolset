from urllib import response
import urllib.request
import urllib.parse


base_url  = 'http://www.baidu.com/s?'

search_data = {
    'wd' : '周杰倫',
    'sex': '男',
    'location': '中國台灣省'
}
#-------------------------
headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
#-------------------------

# 把所有search_data內的資料變為Unicode(網址用)
parsed_search_data = urllib.parse.urlencode(search_data)
# 合併url
url = base_url + parsed_search_data

# custom request object 把headers 帶入custom request 
custom_request = urllib.request.Request(url = url, headers = headers)

# 
response = urllib.request.urlopen(custom_request)
content = response.read().decode('utf-8')
print (content)





