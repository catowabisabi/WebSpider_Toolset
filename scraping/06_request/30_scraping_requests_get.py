# urllib
# (1) 一個類型和六個方法
# (2) get 請求
# (3) post 請求
# (4) ajax 的 get 請求
# (5) ajax 的 post請求
# (6) cookie 登入 請求
# (7) 使用 IP POOL代理

# requests
# (1) 一個類型和六個屬性
# (2) get 請求
# (3) post 請求
# (4) 使用 IP POOL 代理
# (5) cookie 與驗証碼

import requests

# s可以不加
url = 'https://www.baidu.com/s?'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/102.0.0.0 Safari/537.36',
}

data = {
    'wd' : '北京'
}

# url 請求資源路徑
# params 參數
# kwargs 字典

# 提取靜態網站的HTML
response = requests.get(url = url, params = data, headers = headers)
content = response.text
print(content)

# 參數使用params 傳遞
# 參數無需 urlencode
# 不需要custom request
# 請求資源路徑中的?可以加也不加