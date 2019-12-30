from selenium import webdriver
import time
from collections import Counter

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(30)

start = time.time()

while time.time() - start <=60:
    try:
        btn = driver.find_element_by_class_name('main')
        btn.click()
    except:
        pass
