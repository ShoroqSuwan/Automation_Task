import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def google_result(query):
    base_url = "https://www.google.com"
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.maximize_window()  # This is additional (Not required in the task)

    try:
        driver.find_element(By.NAME, "q").send_keys(query)
        driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        result = driver.find_element("tag name", "h3")  # I used both way of finding elements
        act_title = result.text

    except:
        act_title = "no data found"
    driver.quit()
    return act_title
