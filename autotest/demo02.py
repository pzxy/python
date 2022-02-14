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
        # 默认值为By.ID
        # self.driver.find_element("kw").send_keys("selenium")
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        sleep(3)
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        # self.driver.quit()

    def test_name(self):
        # 一个页面可能多个name，但是这里返回第一个。
        self.driver.find_element(By.NAME, "wd").send_keys("selenium")
        sleep(3)
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()

    def test_link_text(self):
        self.test_id()
        # By.PARTIAL_LINK_TEXT,这样只需要输入，'首页'就可以了，没必要用百度首页。
        self.driver.find_element(By.LINK_TEXT, '百度首页').click()
        sleep(3)
        self.driver.quit()

    def test_xpath(self):
        # 检查->选中以后右键，copy-> xpath
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("守望先锋")
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()

    def test_tag(self):
        input0 = self.driver.find_element(By.TAG_NAME, 'input')[0]
        # 一般不用tag定位，因为一个页面tag太多了。
        print(input0)

    def test_css_selector(self):
        # 检查->选中以后右键，copy-> selector
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("日拱一卒")
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()

    def test_class_name(self):
        self.driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("日拱一卒")
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_name()
    # case.test_link_text()
    # case.test_xpath()
    # case.test_css_selector()
    case.test_class_name()
