import re
import urllib.request


url = 'https://blog.csdn.net/m0_69043821/article/details/1250983491'
url2 = 'https://akjdlajkdf.com/kjdfljakd'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',}
try:
    request = urllib.request.Request(url = url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print (content)
except urllib.error.HTTPError:
    print ('出現HTTP Error')
except urllib.error.URLError:
    print ('出現URL Error')