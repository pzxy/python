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

    def test_prop(self):
        print(self.driver.name)  # 浏览器名称
        print(self.driver.current_url)  # url
        print(self.driver.title)  # 判断title来判断是否登录成功了。
        print(self.driver.window_handles)  # 据病，当前窗口。
        print(self.driver.page_source)  # 页面html源码
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "su").click()
        sleep(2)
        self.driver.back()#回退
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()# 前进
        self.driver.close()# 关闭当前tab
        self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    # case.test_prop()
    case.test_method()