import scrapy


class Tc58Spider(scrapy.Spider):
    name = 'tc58'
    allowed_domains = ['sh.58.com']
    start_urls = ['http://sh.58.com/job/?key=%E5%BE%8C%E7%AB%AF&cmcskey=%E5%BE%8C%E7%AB%AF&final=1&jump=1&specialtype=gls']

    def parse(self, response):
        print ('月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
            月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
            月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
            月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔\
            月野仔月野仔月野仔月野仔月野仔月野仔月野仔月野仔')
