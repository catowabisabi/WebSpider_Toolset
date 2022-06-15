import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

#-------------------------
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

        ,#'Accept': '*/*',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'Accept-Language': 'zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6',
        #'Connection': 'keep-alive',
        #'Content-Length': '144',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BAIDUID=18673BE5D5701388B11E44652F5486A3:FG=1; BIDUPSID=18673BE5D5701388B11E44652F5486A3; PSTM=1650410246; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=18673BE5D5701388B11E44652F5486A3:FG=1; H_PS_PSSID=36543_36459_36454_31253_36413_36165_36570_36075_36519_26350_36469_36315; BA_HECTOR=a5852g200l85842h2h1haijum15; ZFY=ooCPX3M4i:BxaT2:A5o45Djt0p6xy7cGOGhXrBnTHWwA4:C; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655263211; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1655263211; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MTUxMzkyNjRhYjhiOGUxYzViNjYyZGM2YzRlZjkwMTUwYTk5MjBiYjBhZTQwNzcwMjk4ZGI3MDRlNzFjNTYzMjk3MjdjNDA4NTY1NDkzODIwN2I5ODE2MjQ1ZDg5NzNhYmExNTdkZmY4ZGFiZDMyOWU3MDJmZmE3YzZlY2U3NWNkNGYyYWU3ZDhiODg3OWQxNjA3YzBhNmRkYWQyZmIyYg==',
        #'Host': 'fanyi.baidu.com',
        #'Origin': 'https://fanyi.baidu.com',
        #'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
        #'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        #'sec-ch-ua-mobile': '?0',
        #'sec-ch-ua-platform': "Windows",
        #'Sec-Fetch-Dest': 'empty',
        #'Sec-Fetch-Mode': 'cors',
        #'Sec-Fetch-Site': 'same-origin',
        #'X-Requested-With': 'XMLHttpRequest'
}
#-------------------------

data =  {
        'from': 'en',
        'to': 'zh',
        'query': 'spider and me',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '153102.439615',
        'token': 'ff2fe9b89b308cad0cf441bc62e5f8ab',
        'domain': 'common'
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

{}