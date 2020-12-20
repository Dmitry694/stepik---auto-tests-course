from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/find_link_text"
a = str(math.ceil(math.pow(math.pi, math.e)*10000))

#print(a)

#link.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    next_link = browser.find_element_by_link_text(a).click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    #button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    time.sleep(15)

    browser.quit()



