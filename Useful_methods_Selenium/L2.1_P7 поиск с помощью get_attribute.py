from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#treasure")
    v_elem = x_element.get_attribute("valuex")
    y = calc(v_elem)

    opt1 = browser.find_element_by_css_selector("#robotCheckbox").click()
    opt2 = browser.find_element_by_css_selector("#robotsRule").click()

    answer = browser.find_element_by_css_selector("#answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()