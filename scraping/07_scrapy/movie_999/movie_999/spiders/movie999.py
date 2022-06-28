from re import M
import scrapy
from movie_999.items import Movie999Item


class Movie999Spider(scrapy.Spider):
    name = 'movie999'
    allowed_domains = ['www.dytt8.net', 'www.dydytt.net']
    start_urls = ['https://www.dydytt.net/html/gndy/china/index.html']

    def parse(self, response):
        
        # 用for loop去拎晒所有野先
        a_list = response.xpath("//div[@class='co_content8']//td[2]//a[2]")
        for a in a_list:
            # 拿第一頁的name和url
            movie_name = a.xpath('./text()').extract_first()
            movie_page_url = a.xpath('./@href').extract_first()
            movie_page_url = 'https://www.dydytt.net'+ movie_page_url

            #進入第二頁 利用meta個名send埋去第二頁度做
            yield scrapy.Request(url=movie_page_url, callback = self.parse_get_movie_page, meta = {'name': movie_name})
        


    def parse_get_movie_page(self, response):
        # span 唔可以用, 因為讀唔到
        movie_image_url = response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        movie_name = response.meta['name']
        
        movie = Movie999Item(src = movie_image_url, name = movie_name )
       
        yield movie
