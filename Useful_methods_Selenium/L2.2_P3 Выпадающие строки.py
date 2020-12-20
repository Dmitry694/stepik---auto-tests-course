from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f_elem = browser.find_element_by_css_selector("#num1").text
    s_elem = browser.find_element_by_css_selector("#num2").text


    f = int(f_elem)
    s = int(s_elem)
    y = (f+s)

    opt1 = browser.find_element_by_css_selector("#dropdown").click()

    answer = browser.find_element_by_css_selector("[value='{}']".format(y)).click()

    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()