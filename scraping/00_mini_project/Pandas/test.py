image_urls = [
  "https://abc.com/abc3.jpg",
  "https://abc.com/abc323.jpg",
  "https://abc.com/abc4.jpg"
]

import pandas as pd
from IPython.display import display

# save the list to dict and then to csv
image_dict = {}
dict_value_list = []

# 把清單中value string變為value list of string (1 list 1 string)
for index, value in enumerate(image_urls):
    dict_value = [value] # 每一個str都變成str in list先
    #新既清單element都放入一個大清單, 方便返pandas做野
    dict_value_list.append(dict_value)

# 清單變為dict, 清單index變為key
for index, value in enumerate(dict_value_list):
    string_format_of_index = str(index+1)
    image_dict[string_format_of_index] = value

#print (image_dict)


df = pd.DataFrame.from_dict(image_dict).transpose()
df.columns =["Images URLs"]
df.to_csv('test.csv' )


