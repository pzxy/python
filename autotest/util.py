from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    driver = webdriver.Chrome(
        service=Service(executable_path="/Users/pzxy/WorkSpace/driver/chromedriver")
    )
    driver.get("https://www.baidu.com")
    get_element(driver, By.ID, "kw").send_keys('selenium')
    get_element(driver, By.ID, "su").click()
    sleep(3)
    driver.quit()
