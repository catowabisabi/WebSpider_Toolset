import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
u = 'https://www.newsnow.co.uk/h/Business+&+Finance'

driver = webdriver.Chrome(executable_path=r"C:\Users\enoma\Desktop\Coding\Python Projects\Cato_Python_Tools\scraping\chromedriver.exe")
driver.maximize_window()
driver.get(u)
time.sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
for i in range(10):
        element =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'btn--primary__label')))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        time.sleep(5)

        print(f'click {i} done')