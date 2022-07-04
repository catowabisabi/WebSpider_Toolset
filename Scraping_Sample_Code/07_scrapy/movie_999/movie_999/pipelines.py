# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Movie999Pipeline:
    
    def open_spider(self, spider):
        self.fp = open('movies.json', 'w', encoding = 'utf-8')


    def process_item(self, item, spider):
        self.fp.write(str(item)+',')
        return item


    def close_spider(self, spider):
        self.fp.close()

  
# import urllib.request
# import socket
# class ImageDownloadPipeline:


#     def process_item(self, item, spider):
        
#         socket.setdefaulttimeout(15)

#         url = 'http:' + item.get('src')
#         print ('\n' + url + '\n')

#         filename = './movie_images/' + item.get('name') + '.jpg'
#         print(filename + '\n')
        
#         try:
#             urllib.request.urlretrieve(url = url, filename = filename)
#         except Exception as e:
#             print("\nerror: " + e + "\n\n")


#         return item

