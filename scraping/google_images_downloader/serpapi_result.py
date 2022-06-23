from encodings import search_function
import os, urllib.request, json
from requests import request # json for pretty output
from serpapi import GoogleSearch
from timeit import default_timer as timer
import eventlet
import pandas as pd

start = timer()

os.environ["API_KEY"] = "8e9269d18e57befb76a74e3e5a13a693b173f7efb8d7b5d71310074c4a864700"


# Downloading images

def download_images(results):
    for index, image in enumerate(results['images_results']):
        print(f'Downloading {index} image...')
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.102 Safari/537.36 Edge/18.19582')]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(image['original'], f'SerpApi_Images/original_size_img_{index+1}.jpg') #零變一

    end = timer()
    print(end - start)

def create_folder(search_query):
    parent_dir = 'C:/Images_downloaded'
    new_dir = '{}'.format(search_query)
    path = os.path.join(parent_dir, new_dir)

    if not os.path.exists(path):
        os.makedirs(path)
        print(f'Folder created : {path}')
    else:
        print('Folder already exists!')
    return path
    


def download_images_in_list(image_results, search_query, path):
    

    opener=urllib.request.build_opener()
    opener.addheaders = [('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    eventlet.monkey_patch()

    for i in range (len(image_results)):
        image_url = image_results[i]
        print (f'({i}) -  {image_url}')
        try:

            with eventlet.Timeout(20, False):
                urllib.request.urlretrieve(url = image_url, filename = path + '/' + search_query + '__' + str(i) +'.jpg')
        except:
            continue


def serpapi_get_google_images(search_query):
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        "api_key": os.getenv("API_KEY"),   # serpapi API key
        "engine": "google",                # search engine. There are also Bing, Yahoo, Naver, Baidu, etc.
        "q": "{}".format(search_query),    # search query
        "gl": "us",                        # country to search from
        "hl": "en",                        # language
        "tbm": "isch",                     # parameter to display image results
        "num": "1000",                      # number of images per page
        "ijn": 0                           # page number, 0 -> first page, 1 -> second and so on
        # other params under API examples: https://serpapi.com/images-results
    }
    
    search = GoogleSearch(params)          # where data extraction happens
    
    image_results = []
    
    images_is_present = True
    while images_is_present:
        
        print(f"Extracted #{params['ijn']} page.")
        
        # JSON -> Python dict (actual data is here)
        results = search.get_dict()

        
    
        # checks for "Google hasn't returned any results for this query."
        if "error" not in results:
            for image in results["images_results"]:
                if image["original"] not in image_results:  
                    image_results.append(image["original"])
            
            # update to the next page
            params["ijn"] += 1
            print(params["ijn"])
            #呢度可以download result但會503

        else:
            images_is_present = False
            print(results["error"])
            
    
    
    print(json.dumps(image_results, indent=2))
    print(len(image_results))
    print(type(image_results)) # List of image urls

    # save the list to dict and then to csv
    image_dict = {}
    dict_value_list = []

    # 把清單中value string變為value list of string (1 list 1 string)
    for index, value in enumerate(image_results):
        dict_value = [value] # 每一個str都變成str in list先
        #新既清單element都放入一個大清單, 方便返pandas做野
        dict_value_list.append(dict_value)

    # 清單變為dict, 清單index變為key
    for index, value in enumerate(dict_value_list):
        string_format_of_index = str(index+1)
        image_dict[string_format_of_index] = value

    #print (image_dict)



    # 生産一個folder
    download_folder_path = create_folder(search_query)

    # 生産image urls 清單, 放到CSV
    df = pd.DataFrame.from_dict(image_dict).transpose()
    df.columns =["Images URLs"]
    df.to_csv('{}/Google_image_search_{}.csv'.format(download_folder_path, search_query))
        


    download_images_in_list(image_results, search_query, download_folder_path)

    print(type(results)) # Dict of image urls
    print(results) # Dict of return response in json
    #print (results['images_results'])

    #個results黎到呢度已經無左
    #download_images(results)

    # -----------------------