import sys
import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.get('https://www.youtube.com/')
time.sleep(3)
search = driver.find_element_by_name('search_query')
search.send_keys('python')
search.send_keys(Keys.ENTER)
