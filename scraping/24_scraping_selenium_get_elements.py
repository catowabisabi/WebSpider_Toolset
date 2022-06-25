from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)
content = browser.page_source

# 利用ID找特定完素
button = browser.find_element_by_id('su')
print (button)

# 利用值找特定完素
button = browser.find_element_by_class_name('wd')

# 利用xpath找特定完素
button = browser.find_element_by_xpaths('//input[@id = "wd"]')
button = browser.find_elements_by_xpaths('//input[@id = "wd"]')

# 利用tag找特定完素
button = browser.find_element_by_tag_name('input')
button = browser.find_elements_by_tag_name('input')

# 利用css找特定完素
button = browser.find_element_by_class_name('#su')
button = browser.find_element_by_class_name('#su')
print (button)

# 利用link text找特定完素
button = browser.find_element_by_link_text('直插')
button = browser.find_element_by_link_text('直插')
print (button)

