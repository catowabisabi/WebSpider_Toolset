import scrapy


class WalmartGrocerySpider(scrapy.Spider):
    name = 'walmart_grocery'
    allowed_domains = ['www.walmart.ca']
    start_urls = ['https://www.walmart.ca/browse/grocery/fruits-vegetables/10019-6000194327370?icid=grocery_wm_OGL1_LMagCategory_Tile_Fruits_Veg']

    def parse(self, response):
        pass
