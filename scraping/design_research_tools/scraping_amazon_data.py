import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep

headers = {
    #'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'accept-encoding':'gzip, deflate, br',
    #'accept-language':'zh-HK,zh;q=0.9,en-GB;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'cookie': 'session-id=139-5538668-8572227; ubid-acbca=132-2111075-8066944; lc-acbca=en_CA; x-acbca="9PTvDQMWVsPqgCq8SQsk1uOyGAK@zvc@@W7l4Em7h46DfAeLOzWcOHcqQvjkcSw3"; at-acbca=Atza|IwEBILIFw_6RXPUlgP7k9Rqewu0RggHPqiFg50SOdeqgCx9J1O_umNcsnvSlkmHsyrn2a0hdaLe60G_w1fVYorfgOv7mz8_YpGI2kYcOhz-MWBDcwFVMY6lFKGFANakz58e0d8IN3G4UxjjRgAzoc7thEBlvI8EjpVB73F18mk1rYZPFxJoBpbOllgVfkZcNTM98y53TMeJDQT331pNmI97I9noi; sess-at-acbca="hitoNW50wd9z/JzSJHaKG2ZaPqmj1QhZBNd0aDfYuaw="; sst-acbca=Sst1|PQEvX2nxmdh5qVfCyUUdlUCdCbvSRiTflFHYm8K0jiWrKV3dD5R_lTSq7RjBYjpeEYfmkCIcQArx6L-ogyCJw07m_-7UoRLNmbZAdd2SX0toDZpiSiNq800t1goRpL-8XJSSbUtSSP8Yldp2zGyY002_UudEsoCKY6pf9OyTzd1zXuW0YDCTnoor4QWqPtIA525TACYJAAuaSyitklMR5HYJcs36JNKW50D0SzXA_xXOz9xYZsl3GPofKUlivDefDg-sa9qtIdBO6wQ_5jBXavcQufUd-iz98ZE12xQ2zBosAKE; session-id-time=2082787201l; i18n-prefs=CAD; csm-hit=tb:ZCMY25P7G3QE625BVVPX+s-ZCMY25P7G3QE625BVVPX|1655930139031&t:1655930139031&adb:adblk_no; session-token=DGxKSh8z3y8Sc4Ni3HQqh4WnWfAvEBLrf/kyYPYSHmv36AgiZncMEugfozEy2HKMtkl7SslhRcLtbv2xF5poj+X+zdqEEaB6j7GdGLhjVxUFe1bRU7IlPpISIVbGusmC6cYSh7mAbPgwa3qUivK3zbsyz0DvIQSHndBK+Ak40BPCSySM0efXXKGtlhwpJ3ao3E/iMfQlxa/EVp/CpTzDFWasmpajYYq+',
    #'device-memory':'8',
    #'downlink':'10',
    #'dpr':'1',
    #'ect':'4g',
    #'referer': 'https://www.amazon.ca/s?k=winter+jacket&page=2',
    #'rtt':'50',
    #'sec-ch-device-memory':'8',
    #'sec-ch-dpr':'1',
    #'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #'sec-ch-ua-mobile':'?0',
    #'sec-ch-ua-platform':'"Windows"',
    #'sec-ch-viewport-width':'1920',
    #'sec-fetch-dest':'document',
    #'sec-fetch-mode':'navigate',
    #'sec-fetch-site':'same-origin',
    #'sec-fetch-user':'?1',
    #'service-worker-navigation-preload':'true',
    #'upgrade-insecure-requests':'1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    #'viewport-width':'1920',

    }

search_query = 'micro usb'.replace (' ','+')
base_url = 'https://www.amazon.ca/s?k={0}'.format(search_query)

items = []

for i in range (1, 3):
    print('Processing {0}...'.format(base_url+'&page={0}'.format(i)))
    
    response = requests.get(base_url+'&page={0}'.format(i), headers = headers)
    print('Processing {0}...{1}'.format(base_url+'&page={0}'.format(i), response.status_code))

    soup = bs(response.content, 'html.parser')

    
    
    #results = soup.find_all('div', {'class' : 's-result-item', 'data-component-type' : 's-search-result'})
    #results = soup.find_all('div', {'class' : 'a-section a-spacing-base a-text-center'})
    results = soup.find_all('div', {'class' : 'a-section a-spacing-base'})
    
    
    for result in results:
        product_name = result.h2.text

        try:
            rating = result.find('span', {'class' : 'a-icon-alt'}).text
            #rating_count_div = result.find_all('div', {'class' : 'a-row a-size-small'})
            #rating_count = rating_count_div.find_all('span', {'aria-label' : True})[2].text
            rating_count = result.find_all('span', {'aria-label': True})[1].text

        except AttributeError:
            continue 

        try:
            price1 = result.find('span', {'class' : 'a-price-whole'}).text
            price2 = result.find('span', {'class' : 'a-price-fraction'}).text
            price = float(price1 + price2)
            product_url = 'https://amazon.ca'+result.h2.a['href']
            items.append([product_name, rating, rating_count, price, product_url])
        except AttributeError:
            continue 
    sleep (1.5)

df = pd.DataFrame(items, columns = ['product','rating','rating count','price','product_url'])
df.to_csv('Amazon_ca_search_({0}).csv'.format(search_query), index = False)

    
