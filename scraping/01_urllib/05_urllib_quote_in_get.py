import urllib.request


# ASCII 編碼 e.g. a = 97, A = 65, 0 = 48

# 這裏的亂碼其實是 Unicode
url = "https://hk-garden.com/forum/categories/"

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

name = '接機台'
name_on_unicode = urllib.parse.quote(name)

modified_url = url + name_on_unicode

# custom request object 這裏不能使用position 
custom_request = urllib.request.Request(url = modified_url, headers = headers)

response = urllib.request.urlopen(custom_request)
content = response.read().decode('utf-8')

print (content)
print (modified_url)