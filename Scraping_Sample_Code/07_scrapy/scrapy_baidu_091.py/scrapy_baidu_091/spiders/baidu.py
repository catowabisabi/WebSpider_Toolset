import scrapy


class BaiduSpider(scrapy.Spider):

    # 爬虫的名字, 用於爬虫時的值
    name = 'baidu'
    # 可以爬的地方
    allowed_domains = ['www.mono12.com']

    # 第一次需要的地方 , 後邊要有斜線
    start_urls = ['https://www.mono12.com/']

    def parse(self, response):
        print('月野三文治')
