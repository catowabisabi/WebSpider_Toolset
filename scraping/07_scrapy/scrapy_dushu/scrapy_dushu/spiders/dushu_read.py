import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 由項目名字的items 中 導入 Item Obj
from scrapy_dushu.items import ScrapyDushuItem

# 創建 scrapy genspider -t crawl dushu_read https://www.dushu.com/book/1188.html

class DushuReadSpider(CrawlSpider):
    name = 'dushu_read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        #d是數字, +是多過一個的數字
        Rule(LinkExtractor( allow=r'/book/1188_\d+\.html'), 
                            callback='parse_item', 
                            follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        img_list = response.xpath ('//div[@class = "bookslist"]//img')

        for img in img_list:
            # 這裏需要使用img而不是response, 另外一定要加點./, 另外要加extract_first()
            name = img.xpath ('./@alt').extract_first()
            src = img.xpath ('./@data-original').extract_first()

            # item obj 裏的值是由我們設定的, 在拿到需要的值後, 要把這些值傳入這個item obj, 再yield 你想yield的item

            #呢兩行一定要係for loop入邊
            book = ScrapyDushuItem(name = name, src = src)
            yield book
