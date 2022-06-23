from encodings import search_function
import os, urllib.request, json
from requests import request # json for pretty output
from serpapi import GoogleSearch
from timeit import default_timer as timer

start = timer()

os.environ["API_KEY"] = "0ffc61a619905fad4568c79bd42e0d90acb9a030f9cc012a29e70dcf91a5a014"


# Downloading images

def download_images(results):
    for index, image in enumerate(results['images_results']):
        print(f'Downloading {index} image...')
        
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.102 Safari/537.36 Edge/18.19582')]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(image['original'], f'SerpApi_Images/original_size_img_{index}.jpg')

    end = timer()
    print(end - start)

def download_images_in_list(image_results, search_query):

    parent_dir = 'C:/Images_downloaded'
    new_dir = '{}'.format(search_query)
    path = os.path.join(parent_dir, new_dir)

    if not os.path.exists(path):
        os.makedirs(path)
        print(f'Folder created : {path}')
    else:
        print('Folder already exists!')
    

    opener=urllib.request.build_opener()
    opener.addheaders = [('User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')]
    urllib.request.install_opener(opener)


    for i in range (len(image_results)):
        image_url = image_results[i]
        print (f'({i}) -  {image_url}')
        try:
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
        "num": "100",                      # number of images per page
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

    download_images_in_list(image_results, search_query)

    print(type(results)) # Dict of image urls
    print(results) # Dict of return response in json
    #print (results['images_results'])

    #個results黎到呢度已經無左
    #download_images(results)

    # -----------------------