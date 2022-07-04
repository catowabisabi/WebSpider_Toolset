# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用pipeline, 就要在setting 開啓左先
class ScrapyDangdangPipeline:

    def open_spider(self, spider):
        
        #在運行spider之前, 先打開一個文件
        self.fp = open('book.json', 'w', encoding = 'utf-8')

    # 這個item就是在yield 後邊的obj
    def process_item(self, item, spider):


            # save成為json write一定要是string
            # w 會每次都save, 會delete左之前既info, 所以要用a
            # 每次都開文件會有hang機
        # with open ('book.json', 'a', encoding='utf-8') as fp:
        #    fp.write(str(item))

        #寫入之前的文件
        self.fp.write(str(item))

        return item


    def close_spider(self, spider):
        self.fp.close()

# 同時開始幾個pipeline

# 下載圖片 可以使用urllib
import urllib.request
import socket
class DangDangDownloadPipeline:

    # 定義pipeline 類別
    # 要加入settings
    # item唔可以有S
    def process_item(self, item, spider):
        
        socket.setdefaulttimeout(15)

        #要加返http:
        url = 'http:' + item.get('src')
        print (url)

        # 要加返/
        filename = './book_images/' + item.get('name') + '.jpg'
        print(filename + '\n')
        try:
            urllib.request.urlretrieve(url = url, filename = filename)
        except Exception as e:
            print("\nerror: " + e + "\n\n")

        # 要item
        return item

