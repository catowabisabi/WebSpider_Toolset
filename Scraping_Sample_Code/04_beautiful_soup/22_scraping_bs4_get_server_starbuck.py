import urllib.request
import urllib.error
from bs4 import BeautifulSoup as bs
#import dryscrape # 由於呢個網係用JS寫, 所以唔可以用urllib


url = "https://www.starbucks.com.cn/menu"
#url_json = "https://www.starbucks.ca/bff/ordering/menu"

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

def get_elements(content, elements_id):
    try:
        soup = bs(content, 'lxml')
        try:
            elements = soup.select(elements_id)
        except:
            print('soup.find: Error')
        return elements
    except:
        print('get_elements : Error')



def main(url):

    #先定義xpath
    #product_big_cat = "food" #"drinks" / "food" / "at-home" / "merchandise" /
    #xpath_product_cat_title_list = "//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//@data-e2e".format(product_big_cat)
    #xpath_product_cat_image_list ="//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//img[@class = 'imageBlock___3sr1L sb-imageFade__imagePositioning sb-imageFade__show']/@src".format(product_big_cat)
    #xpath_product_cat_url_list = "//section[@id ='{}']/div[@class ='grid grid--compactGutter']//div[@class ='mb3 lg-mb5 gridItem size12of12 md-size6of12']/div[@class = 'flex items-center']//a".format(product_big_cat)
    
    #bs_path_product_cat_title_list = '"section", id = "{}" '.format(product_big_cat)

    xpath_product_name_list_element_id = '//ul[@class ="grid padded-3 product"]//strong/text()'
    bs_path_product_name_list_element_id = 'ul[class = "grid padded-3 product"] strong'

    content = get_html_content(url)
    #print(content)
    
    product_name_list = get_elements(content, bs_path_product_name_list_element_id)

    for product in product_name_list:
        product = product.string
        #product = product.get_text()

        print (product)
    

main(url)