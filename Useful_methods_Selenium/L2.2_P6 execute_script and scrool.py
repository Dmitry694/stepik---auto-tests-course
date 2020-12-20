from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = " http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    f_elem = browser.find_element_by_css_selector("#input_value").text
    y = calc(f_elem)

    inpt = browser.find_element_by_tag_name("input").send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    f_click = browser.find_element_by_tag_name("body > div > form > div.form-check.form-check-custom > label").click()

    rbts_r = browser.find_element_by_tag_name("body > div > form > div.form-check.form-radio-custom > label").click()

    btn = browser.find_element_by_tag_name("body > div > form > button").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
assert True