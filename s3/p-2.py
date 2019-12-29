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

driver.get('http://www.encar.com/index.do')
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_id('manufact').click()

driver.find_element_by_xpath('//*[@id="manufactListText"]/ul[2]/li[24]/a').click()
driver.find_element_by_xpath('//*[@id="seriesItemList"]/li[6]/a').click()
driver.find_element_by_xpath('//*[@id="mdlItemList"]/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a').click()

driver.quit()
