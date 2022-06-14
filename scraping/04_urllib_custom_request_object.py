import urllib.request

url_page = 'https://www.baidu.com'

# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E5%80%AB&fenlei=256&rsv_pq=bfd3478e00038d2f&rsv_t=7b19xJqRTGYey8k%2Fjbp2wsWuh1zCO5LYs3qQuTVii8bqwrx8uJTRPmPpsfk&rqlang=cn&rsv_dl=tb&rsv_sug3=24&rsv_enter=1&rsv_sug1=10&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%2591%25A8%25E6%259D%25B0%25E5%2580%25AB&rsp=6&inputT=7102&rsv_sug4=7211

#url 的組成
# http / https     www.baidu.com     80/443         s           wd = 周杰倫         #
# 協定                  主機           端口        路徑                參數           錨點
# http      80
# https     443
# mysql     3306
# oracle    1521
# redis     6379
# mongodb   27017

url = 'https://hk-garden.com/forum/'

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# custom request object 這裏不能使用position 
custom_request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(custom_request)
content = response.read().decode('utf-8')
print (content)