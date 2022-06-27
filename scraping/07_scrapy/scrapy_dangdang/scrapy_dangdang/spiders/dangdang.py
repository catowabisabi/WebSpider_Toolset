import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ["www.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.49.01.16.00.00.html"]

    def parse(self, response):
        



        li_list = response.xpath("//ul[@id = 'component_59']/li")

        for li in li_list:

            src = li.xpath('.//img/@sata-original').extract_first()

            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(".//p[@class ='price']/span[1]/text()").extract_first()

            print (src, name, price)


