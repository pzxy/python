from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(executable_path="/Users/pzxy/WorkSpace/driver/chromedriver")
        )
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        sleep(3)
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_id()
