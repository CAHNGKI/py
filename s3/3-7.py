import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')

driver.implicitly_wait(5)

driver.get('http://google.com')

driver.save_screenshot('C:/Users/moon2/Desktop/file/py/s3/webdriver/website1.png')

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot('C:/Users/moon2/Desktop/file/py/s3/webdriver/website2.png')

driver.quit()
