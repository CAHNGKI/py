from selenium import webdriver
import time
from collections import Counter

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(30)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')

def analysis():

    btns_rgba =[btn.value_of_css_property('background-color') for btn in btns]

    result = Counter(btns_rgba)

    for key, value in result.items():
        if value ==1:
            answer = key
            break

        else:
            answer = None


    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()


start =time.time()
while time.time() - start <=60:
    analysis()
