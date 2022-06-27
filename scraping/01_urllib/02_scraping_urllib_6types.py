import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

#print(type(response)) # <class 'http.client.HTTPResponse'>

content = response.read(50) # return 50 個字節
#print (content)


content = response.readline() 
#print (content)

content = response.readlines() 
#print (content)

content = response.getcode() # return 200 404 500 etc.
print (content)

content = response.geturl() # return url.
print (content)

content = response.getheaders() # return 狀態信息.
print (content)