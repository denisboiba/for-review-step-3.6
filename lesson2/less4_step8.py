import pyperclip
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    url = 'http://suninjuly.github.io/explicit_wait2.html'

    browser.get(url)

    trigger = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    # copy answer to clipboard
    txt_answer_alert = browser.switch_to.alert.text
    my_answer = txt_answer_alert.split(': ')[-1]
    pyperclip.copy(my_answer)  # copy to clipboard
    browser.switch_to.alert.accept()

finally:
    time.sleep(2)
    browser.quit()


