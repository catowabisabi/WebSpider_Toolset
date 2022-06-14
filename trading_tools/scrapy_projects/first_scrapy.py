from urllib import response
import scrapy

# Example NewsSpider spider
class NewsSpider(scrapy.Sider):
    name = 'news'

# Selector for links
links = response.xpath('//a/@href0')

#Selector for divs
divs = response.xpath('//div')

#Selector for paragraphs
paragraphs = response.xpath('//p/')


# Example Item class
class Article(scrapy.Item):
    headline = scrapy.Field()