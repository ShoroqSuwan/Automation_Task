import time

from selenium import webdriver
from selenium.webdriver import Keys


def yahoo_result(query):
    base_url = "https://www.yahoo.com"
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.maximize_window()

    try:
        driver.find_element("name", "p").send_keys(query)
        driver.implicitly_wait(2)
        driver.find_element("name", "p").send_keys(Keys.ENTER)
        time.sleep(2)
        result = driver.find_element("xpath", "//h3/a")
        time.sleep(2)
        site_title = result.text
        driver.implicitly_wait(2)

    except:
        act_title = "no data found"

    driver.quit()
    return site_title[15:36]
