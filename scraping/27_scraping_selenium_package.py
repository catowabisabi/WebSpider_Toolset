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

def share_browser():
    # 設定chrome driver的location
    ser = Service("chromedriver.exe")

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

    return driver

browser = share_browser()

# 設定要使用的網址
url = 'https://www.google.com'
    
# 利用web driver去拎網址
browser.get(url)

# 拿HTML
pageSource = browser.page_source
with open("page_source.html", "w", encoding= "utf-8") as f:
    f.write(pageSource)


fileToRead = open("page_source.html", "r", encoding= "utf-8")
print(fileToRead.read())
fileToRead.close()
browser.quit()
