import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1655847806137_101&jsoncallback=jsonp102&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 

    'cookie': 't=d0a806c3033cc7251b4afe7dbd660457; cna=OrOuGnETKRsCAWPk7L57ekQe; tracknick=marshallmatta; enc=ZXQy669zGqDcKsxxG4GGOTKAGu9CV5ugvakWdTy6dfux7BuzTotg2xxFnP3Y43cO0jKvv8qUvPwVIl90XJZomg%3D%3D; thw=ca; sgcookie=E100%2BYew1cuKzP6bbvjs%2BzjyuVsJ5rwmJd7ZEeoIXXB66YSVFYgBNCrFyg3IF4rOacgIw3QTQKhUchsF2L36O%2BlaEOQsPOGulxblKpFP9KFCdppDicu2gQiiGqk0oNlBpvUE; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=DlG0yhV8dKFL4xDJQA%3D%3D&vt3=F8dCvCwhnPEy5lNl3tg%3D&id2=UUwSDCrxvGuLfg%3D%3D; lgc=marshallmatta; uc4=nk4=0%40DDSlAupLDJRVeV2cq%2B7XlIKw1Mm6fml4&id4=0%40U27NBZLNIAUmFyL7GERBbjQpJFAG; _cc_=Vq8l%2BKCLiw%3D%3D; cookie2=212f21b431fc2f8b2c3fb49f370ff18b; v=0; _tb_token_=ee3957366b31f; xlly_s=1; tb_city=330100; tb_cityName="urzW3Q=="; tfstk=cpTVBFMw2q3q3RQsvZ_ZGpoMqSWAZwdDszWPmvPMeKu7mtsciqeOZHh1atPzIif..; l=eBgT5auugXxkPP2XBOfZhurza77TMIRAguPzaNbMiOCP_h1e5vMAW6bV9MLwCnMNhstHR3SVatiMBeYBq5vsjqj4axom4JDmn; isg=BD4-QXt10Fv6kgdFCRI-bykKj1SAfwL5S2fI1ehH0wF8i95lUA-5CTTlB09Hs_oR',


    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6',

    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.2.52b9112awp8emI&city=310100',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',

    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url = url, headers= headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

#切頭
content = content.split('(')[1]

#切尾
content = content.split(')')[0]


with open ('test.json', 'w', encoding='utf-8') as fp:
    fp.write(content)


import json
import jsonpath

obj = json.load(open('test.json',  encoding="utf-8"))
city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)