import unittest
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
lns = (link1, link2)

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        for ln in lns:
            self.browser.get(ln)

            each_fn = self.browser.find_element_by_css_selector(
                "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Ivan")
            #try:
            search_ln = self.browser.find_element_by_css_selector(
                "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Dorn")
            #except Exception:
            #    pass
            search_em = self.browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("123@123.ru")
            button = self.browser.find_element_by_css_selector("button.btn").click()

            welcome_text_elt = self.browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            a = ln
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "test down =( {}".format(a))

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

