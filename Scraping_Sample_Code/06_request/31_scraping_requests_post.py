import requests
import json


url = 'https://fanyi.baidu.com/sug'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/102.0.0.0 Safari/537.36',
}

data = {
    'kw' : 'eye'
}

# url 請求資源路徑
# data 參數

# 提取靜態網站的HTML POST
response = requests.post(url = url, data = data, headers = headers)
content = response.text

obj = json.loads(content) # 這裏有可能會亂碼


print(obj)

# 參數使用data 傳遞
# 參數無需 urlencode
# 不需要custom request
