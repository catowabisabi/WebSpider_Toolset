from logging import exception
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 設定chrome driver的location
ser = Service("chromedriver.exe")

# 設定要使用的網址
url = 'https://www.google.com'

# 設定user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

#設定options
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')



# 開啓 web driver
#driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver = webdriver.Chrome(service = ser, options=options)
driver.implicitly_wait(0.5)

# 利用web driver去拎網址
driver.get(url)
driver.get_screenshot_as_file("screenshot.png")

#確定現時的URL
get_url = driver.current_url
print(str(get_url))

#print(driver.title)

try:
    searchbar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    searchbar.send_keys('elon musk')
    time.sleep(0.2)
    searchbar.send_keys(Keys.ENTER)
    
except:
    print('error')

time.sleep(2)

#news_button = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.XPATH, "//a[@data-hveid='CAEQAw']"))
#)
news_button = driver.find_element(By.LINK_TEXT, "新聞")
news_button.click()
time.sleep(2)


    # Scoll Down to the bottom of the page
def scroll_to_bottom():
    scroll_origin = ScrollOrigin.from_viewport(10, 10)
    ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0, 100000)\
            .perform()
    time.sleep(2)

# 按google的頁碼
def click_page(page_number):
    page_button = driver.find_element(By.XPATH, "//a[@aria-label = 'Page {}']".format(page_number))
    page_button.click()
    time.sleep(2)

# 按下一頁
def click_next_page():
    next_page_button = driver.find_element(By.LINK_TEXT, "下一頁")
    next_page_button.click()
    time.sleep(2)

def get_page_source_code():
    content = driver.page_source()
    return content

scroll_to_bottom()
driver.get_screenshot_as_file("screenshot1.png")
#content = get_page_source_code()
#print(str(content))

click_next_page()
scroll_to_bottom()
driver.get_screenshot_as_file("screenshot2.png")
click_page(6)
driver.get_screenshot_as_file("screenshot3.png")
scroll_to_bottom()
click_next_page()
scroll_to_bottom()
driver.back()
driver.forward()
scroll_to_bottom()

time.sleep(10)
driver.quit()