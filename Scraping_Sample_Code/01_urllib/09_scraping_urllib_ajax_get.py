import urllib.request

from requests import request

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        #'Cookie': 'BAIDUID=18673BE5D5701388B11E44652F5486A3:FG=1; BIDUPSID=18673BE5D5701388B11E44652F5486A3; PSTM=1650410246; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=18673BE5D5701388B11E44652F5486A3:FG=1; H_PS_PSSID=36543_36459_36454_31253_36413_36165_36570_36075_36519_26350_36469_36315; BA_HECTOR=a5852g200l85842h2h1haijum15; ZFY=ooCPX3M4i:BxaT2:A5o45Djt0p6xy7cGOGhXrBnTHWwA4:C; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655263211; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1655263211; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MTUxMzkyNjRhYjhiOGUxYzViNjYyZGM2YzRlZjkwMTUwYTk5MjBiYjBhZTQwNzcwMjk4ZGI3MDRlNzFjNTYzMjk3MjdjNDA4NTY1NDkzODIwN2I5ODE2MjQ1ZDg5NzNhYmExNTdkZmY4ZGFiZDMyOWU3MDJmZmE3YzZlY2U3NWNkNGYyYWU3ZDhiODg3OWQxNjA3YzBhNmRkYWQyZmIyYg==',
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open ('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
#fp = open('douban.json', 'w', encoding='utf-8')
#fp.write(content)