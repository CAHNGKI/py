
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.get('http://zzzscore.com/1to50/?ts=1577599875435')
driver.implicitly_wait(5)

num = 1
def clickbtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        if btn.text == str(num):
            btn.click()
            num +=1
            return

while num <=50:
    clickbtn()
