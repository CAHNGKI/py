import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = "utf-8")

class ncafewrite:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/Users/moon2/Desktop/file/py/s3/webdriver/chromedriver")


    def writeattendcheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        self.driver.find_element_by_name('id').send_keys('moon20517')
        self.driver.find_element_by_name('pw').send_keys('Ansc112!')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=10121064&search.menuid=494')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('hi')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)
    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    a =ncafewrite()
    start_time = time.time()
    a.writeattendcheck()
    del a
