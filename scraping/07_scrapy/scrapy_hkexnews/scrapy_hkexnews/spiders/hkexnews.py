import scrapy


class HkexnewsSpider(scrapy.Spider):
    name = 'hkexnews'
    allowed_domains = ['www.hkexnews.hk']
    start_urls = ['https://www.hkexnews.hk/index_c.html']

    def parse(self, response):
        print(
'月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔'
)
        # HTML 字串
        content = response.text
        # HTML 二進制
        content = response.body
        print(content)

        elements = response.selector.xpath("//ul[@class ='box_content_area']/li[1]//div[@class = 'box_content_area-left-date'][1]/text()").get()
        print(elements)
