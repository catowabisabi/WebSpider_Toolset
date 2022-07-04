import urllib.request

url = 'https://www.facebook.com/carsonto20/about'
headers = {
'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding':' gzip, deflate, br',
'accept-language':' zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6',
'cache-control':' max-age=0',
'cookie':' sb=TaIoYgD8ja0uB1emBuqSQBbT; datr=KwoqYrNfmDj-bJoylzWKR4B6; c_user=100074811618293; xs=5%3A400dZEM4vjPvtg%3A2%3A1653661114%3A-1%3A13399%3A%3AAcVGaQI9eApc-hON1FVqHeBEQ9Rvc-fP9PDnIhDhIMs; fr=0Guwiu1N2XxZx6S0F.AWW-zastKYQC3rjehJRf1Fv1jZo.Birmxz.CZ.AAA.0.0.BirnX1.AWWoIHQ7Ewk; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1655601207223%2C%22v%22%3A1%7D',
'sec-ch-prefers-color-scheme':' light',
'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
'sec-ch-ua-mobile':' ?0',
'sec-ch-ua-platform':' "Windows"',
'sec-fetch-dest':' document',
'sec-fetch-mode':' navigate',
'sec-fetch-site':' same-origin',
'sec-fetch-user':' ?1',
'upgrade-insecure-requests':' 1',
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'viewport-width':' 1920',
'Content-Type': 'text/html; charset=utf-8' 
}

request = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gb2312')
with open ('facebook.html', 'w', encoding='gb2312') as fp:
        fp.write(content)
print (content)