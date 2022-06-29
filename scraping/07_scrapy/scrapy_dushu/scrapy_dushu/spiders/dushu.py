import scrapy
from scrapy.linkextractors import LinkExtractor


class DushuSpider(scrapy.Spider):
    name = 'dushu'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188.html']

    def parse(self, response):
        #\d+ 是 數字的表達式
        page_urls = LinkExtractor(allow = r'/book/1188_\d+\.html')
        a = page_urls.extract_links(response)

        # 這裏不要加@href, no @href
        page_urls = LinkExtractor(restrict_xpaths= r'//div[@class = "pages"]//a')
        a = page_urls.extract_links(response)



        print (a)

