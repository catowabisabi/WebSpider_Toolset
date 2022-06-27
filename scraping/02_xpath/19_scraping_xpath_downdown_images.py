# 在站長素材下載前十頁的圖片

import urllib.request
from lxml import etree

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/tiankongtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/tiankongtupian_'+str(page)+'.html'
    
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    
    request = urllib.request.Request(url = url, headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def get_image_links_and_download(content):
    #拿網頁結構
    tree = etree.HTML(content)
    #
    list_of_image_urls = tree.xpath('//div[@id = "container"]//a/img/@src') #有時候會變SRC2 
    list_of_image_names = tree.xpath('//div[@id = "container"]//a/img/@alt')
    
    # list 0 - 39 
    for i in range (len(list_of_image_names)):
        name = list_of_image_names[i]
        image_url = 'https:' + list_of_image_urls[i]
        print (name, image_url)

        urllib.request.urlretrieve(url = image_url, filename ='./19_download_images/'+name+'.jpg')




if __name__ == '__main__':
    start_page = int(input('請輸入開始的頁碼'))
    end_page = int(input('請輸入結束的頁碼'))

    for page in range (start_page, end_page+1):

        #定制request
        request = create_request(page)
        #拿全個網頁 (每個page)
        content = get_content(request)

        get_image_links_and_download(content)


    









