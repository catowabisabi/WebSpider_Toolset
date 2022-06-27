import scrapy


class HkWarrentsSpider(scrapy.Spider):
    name = 'hk_warrents'
    allowed_domains = ['hk.warrants.com']
    start_urls = ['http://hk.warrants.com/']

    def parse(self, response):
        content = response.text
        print('+++++++++++++++++++++++++++++++++++++++++++++++\n\n')
        print(content)
