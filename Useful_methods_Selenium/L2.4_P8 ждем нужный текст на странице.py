from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока прайс не будет = $100
button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
click = browser.find_element_by_css_selector("#book").click()

x = browser.find_element_by_css_selector("#input_value")
y = x.text
xy = calc(y)

answear = browser.find_element_by_css_selector("#answer").send_keys(xy)

button2 = browser.find_element_by_css_selector("body > form > div > div > button").click()

time.sleep(10)
browser.quit()