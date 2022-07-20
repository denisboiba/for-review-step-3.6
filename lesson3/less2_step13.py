import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, url):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(url)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys('Test')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys('Test')
        input3 = browser.find_element(By.CSS_SELECTOR, '.third_class .third')
        input3.send_keys('tt@gmail.com')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_registration1(self):
        url = "http://suninjuly.github.io/registration1.html"
        expected_res = "Congratulations! You have successfully registered!"
        registration1_res = self.fill_form(url)
        self.assertEqual(registration1_res, expected_res)

    def test_registration2(self):
        url = "http://suninjuly.github.io/registration2.html"
        expected_res = "Congratulations! You have successfully registered!"
        registration2_res = self.fill_form(url)
        self.assertEqual(registration2_res, expected_res)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
