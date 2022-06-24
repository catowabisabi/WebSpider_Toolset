import urllib.request
import urllib.error
from bs4 import BeautifulStoneSoup as bs


url = "https://www.starbucks.ca/menu"

def get_html_content(url):

    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        print(('\nHTML Content Downloaded From :{}, Response Code = {}\n\n').format(url, response.code))
        return content
        
    except urllib.error.URLError as e:
        print(('\nHTML Content Download Fail, Response Code = {}\n\n').format(e))
    except urllib.error.HTTPError as e:
        print(('\nHTML Content Download Fail, Response Code = {}\n\n').format(e))

def get_elements(content, xpath_elements):
    soup = bs(content, 'lxml')
    elements = soup.find(xpath_elements)
    return elements



def main(url):

    #先定義xpath
    product_big_cat = "food" #"drinks" / "food" / "at-home" / "merchandise" /
    xpath_product_cat_title_list = "//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//@data-e2e".format(product_big_cat)
    xpath_product_cat_image_list ="//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//img[@class = 'imageBlock___3sr1L sb-imageFade__imagePositioning sb-imageFade__show']/@src".format(product_big_cat)
    xpath_product_cat_url_list = "//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//a".format(product_big_cat)
    
    content = get_html_content(url)
    product_cat_title_list = get_elements(content, xpath_product_cat_title_list)
    print (product_cat_title_list)
    


main(url)