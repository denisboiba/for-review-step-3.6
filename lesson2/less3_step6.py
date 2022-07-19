import math
import pyperclip
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    url = 'http://suninjuly.github.io/redirect_accept.html'

    browser.get(url)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    # copy answer to clipboard
    txt_answer_alert = browser.switch_to.alert.text
    my_answer = txt_answer_alert.split(': ')[-1]
    pyperclip.copy(my_answer)  # copy to clipboard
    browser.switch_to.alert.accept()

finally:
    time.sleep(2)
    browser.quit()


