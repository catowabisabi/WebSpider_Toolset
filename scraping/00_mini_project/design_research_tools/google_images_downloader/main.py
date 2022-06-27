from bs4_content_type_img import get_images_with_request_headers
from bs4_original_images import get_original_images
from bs4_suggested_search import get_suggested_search_data
from serpapi_result import serpapi_get_google_images

search_query = input('Name the images you want to download from Google: ')

#get_original_images(search_query)
#get_suggested_search_data(search_query)
#get_images_with_request_headers(search_query)

serpapi_get_google_images(search_query)