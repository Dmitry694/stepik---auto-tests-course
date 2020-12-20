from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Заполняем обязательные поля
    fn = browser.find_element_by_class_name("form-control.first").send_keys("Ivan")
    ln = browser.find_element_by_class_name("form-control.second").send_keys("Dorn")
    em = browser.find_element_by_class_name("form-control.third").send_keys("123@123.ru")
    #отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

    time.sleep(5)

    #находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    #Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()


