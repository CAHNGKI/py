import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

chrome_option= Options()
chrome_option.add_argument('--headless')

driver = webdriver.Chrome(chrome_option=chrome_option,executable_path='C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
#driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
#driver.set_window_size(1920,1280)
#driver.implicitly_wait(5)

driver.get('http://google.com')
time.sleep(5)

driver.save_screenshot('C:/Users/moon2/Desktop/file/py/s3/webdriver/website1.png')

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
time.sleep(5)

driver.save_screenshot('C:/Users/moon2/Desktop/file/py/s3/webdriver/website2.png')

driver.quit()
