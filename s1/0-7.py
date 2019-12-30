from selenium import webdriver
import time
from collections import Counter

driver = webdriver.Chrome('C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver')
driver.get('https://tgd.kr/clips/419009?page=1')
driver.implicitly_wait(5)
time.sleep(3)

url_element = driver.find_element_by_xpath('//*[@id="video-playback"]/div[1]/video')
vid_url = url_element.get_attribute('src')

title_element = driver.find_element_by_id('clip-title')
title = title_element.get_attribute('a')

import re
title = re.sub('[^0-9a-zA-Zㄱ-핧]','',title)

from urllib.request import urlretrieve
urlretrieve(vid_url, title+'.mp4')
driver.close()
