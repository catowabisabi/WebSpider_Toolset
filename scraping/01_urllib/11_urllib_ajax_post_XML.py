import urllib.request
import urllib.parse


def create_request(page):
    #要提取資料的URL, 不改變的部份
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': page,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8') #get 後邊不用加encode, post是需要的
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',}
    request = urllib.request.Request(url = base_url, headers = headers, data = data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open ('kfc_'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程式入口
if __name__ == '__main__':
    start_page = int(input("請輸入開始的頁數"))
    end_page = int(input("請輸入結束的頁數"))

    for page in range (start_page, end_page + 1):
        require = create_request(page)
        content = get_content(require)
        down_load(page, content)