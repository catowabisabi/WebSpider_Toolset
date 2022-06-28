from pkg_resources import yield_lines
import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.49.01.16.00.00.html']

    # 拿每一頁
    #
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        src = response.xpath("//ul[@id = 'component_59']/li//img/@src")
        alt = response.xpath("//ul[@id = 'component_59']/li//img/@alt")
        price = response.xpath("/ul[@id = 'component_59']/li//p[@class ='price']/span[1]/text()")

        # 所有的selector的對像都可以再次調用xpath方法

        li_list = response.xpath("//ul[@id = 'component_59']/li")

        for li in li_list:
            #如果有懶加載可以checkcheck, 第一張圖片和其他的不一樣, SRC
            src = li.xpath('.//img/@data-original').extract_first()

            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(".//p[@class ='price']/span[1]/text()").extract_first()

            print (src, name, price)

            # 把拿到的東西放到book obj (ScrapyDangdangItem)
            book = ScrapyDangdangItem(src = src, name = name, price = price)

            # 每當拿到一個book就交給pipeline
            yield book
        
        if self.page < 100:
            self.page += 1

            url = self.base_url + str(self.page) + '-cp01.49.01.16.00.00.html'

            #再做多次
            yield scrapy.Request(url = url, callback = self.parse)


