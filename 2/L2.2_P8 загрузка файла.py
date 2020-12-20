from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/file_input.html"
    browser.get(link)

    f_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)").send_keys("Zzz")
    l_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)").send_keys("Yyy")
    email = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)").send_keys("123@123.ru")

    att = browser.find_element_by_css_selector("#file").send_keys(r"Y:\selenium_course\2\test.txt")

    btn = browser.find_element_by_css_selector("body > div > form > button").click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
assert True