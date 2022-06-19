import urllib.parse
import urllib.request

url = 'page_limit=20&page_start={movies_number_in_page}'



# 做一個custom 
def create_request(page):
    #要提取資料的URL, 不改變的部份
    base_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'

    data = {
        'page_start': (page - 1)*20,
        'page_limit': 20
    }

    data = urllib.parse.urlencode(data) #get 後邊不用加encode, post是需要的
    url = base_url + data
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',}
    request = urllib.request.Request(url = url, headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open ('douban'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程式入口
if __name__ == '__main__':
    start_page = int(input("請輸入開始的頁數"))
    end_page = int(input("請輸入結束的頁數"))

    for page in range (start_page, end_page + 1):
        require = create_request(page)
        content = get_content(require)
        down_load(page, content)




