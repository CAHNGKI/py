import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.set_window_size(1920,1280)
driver.implicitly_wait(5)

driver.get('https://www.wishket.com/accounts/login/')
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_name('identification').send_keys('moon20517')
driver.find_element_by_name('password').send_keys('00000000')
driver.find_element_by_xpath('//*[@id="submit"]').click()

driver.quit()
