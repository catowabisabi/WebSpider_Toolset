
import requests
from bs4 import BeautifulSoup as bs
import urllib.request

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/102.0.0.0 Safari/537.36',
}

# 打一個錯的密碼去拿登入接口

url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
url_to_get_viewstate = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"


# 先要拿必要的登入資料 requests
response = requests.get(url = url_to_get_viewstate, headers = headers)
content = response.text

# 用BeautifulSoup 的lxml去解釋文件, 這裏可以使用其他都可以, 沒什麼所謂
soup = bs(content, 'lxml')
# ID中的value
viewstate_data = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator_data = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print('\n\nviewstategenerator_data : '+viewstategenerator_data+'\n\n')
print('\n\nviewstate_data: '+viewstate_data+'\n\n')

# 拿到驗証碼的圖片

code_img_url = soup.select('#imgCode')[0].attrs.get('src')
code_img_url = 'https://so.gushiwen.cn' + code_img_url


# 下載驗証碼 這個圖片不能對上下邊的請求, 因為下邊的請求是第二個請求
urllib.request.urlretrieve(url = code_img_url, filename = 'code.jpg')
# 所以我們要通過session去保持兩個請求一致
session = requests.session
# 拿這個url的內容, 驗証碼
code_response = session.get(code_img_url)
# 拿取圖片的2進制數據
code_content = code_response.content
# 
with open ('code.jpg', 'wb') as fp:
    fp.write(code_content)




image_code = input ('Please type in the code: ')

# 正式登入
user_email                  =   'abc@gmail.com'
user_password               =   '1234567'

data = {
    '__VIEWSTATE'           :   viewstate_data,
    '__VIEWSTATEGENERATOR'  :   viewstategenerator_data,
    'from'                  :   'http://so.gushiwen.cn/user/collect.aspx',
    'email'                 :   user_email,
    'pwd'                   :   user_password,
    'code'                  :   image_code,
    'denglu'                :   '登录',
}

# requests
response_post = session.post(url = url, headers = headers, data = data)
content_post = response.text

with open('gushiwen.html', 'w', encoding = 'utf-8') as fp:
    fp.write(content_post)



