from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    f_click = browser.find_element_by_css_selector("body > form > div > div > button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value")
    y = x.text
    xy = calc(y)

    answear = browser.find_element_by_css_selector("#answer").send_keys(xy)

    button = browser.find_element_by_css_selector("body > form > div > div > button").click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
assert True