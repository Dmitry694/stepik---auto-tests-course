from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
        element.send_keys("My answear")

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()