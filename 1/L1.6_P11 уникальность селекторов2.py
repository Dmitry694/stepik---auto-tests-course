from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Заполняем обязательные поля
    fn = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Ivan")
    ln = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Dorn")
    em = browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input").send_keys("123@123.ru")

    #отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)

    #находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    #Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

