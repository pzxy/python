from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(executable_path="/Users/pzxy/WorkSpace/driver/chromedriver")
        )
        # 一个测试网站
        self.driver.get("http://sahitest.com/demo/linkTest.htm")
        self.driver.maximize_window()

    def test_webelement_prop(self):
        e = self.driver.find_element(By.ID, 't1')
        print(e.id)
        print(e.tag_name)  # tag名称
        print(e.size)  # 宽高
        print(e.rect)  # 宽高和坐标，矩形框
        print(e.text)  # 文本

    def test_webelement_method(self):
        e = self.driver.find_element(By.ID, 't1')
        e.send_keys('hello world')
        sleep(2)
        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        # css中的一些属性
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()

    def test_webelement_method2(self):
        form_element = self.driver.find_element(By.XPATH, '/html/body/form[1]')
        form_element.find_element(By.ID, 't1').send_keys('通过form表单定位')


if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_webelement_method2()
