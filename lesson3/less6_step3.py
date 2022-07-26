import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSentence:
    sentence = ''

    @pytest.fixture(scope="session")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        print(self.sentence)
        browser.quit()

    @pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_create_sentence(self, browser, number):
        url = f'https://stepik.org/lesson/{number}/step/1'
        browser.get(url)
        browser.implicitly_wait(10)

        input1 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        answer = math.log(int(time.time()))
        input1.send_keys(answer)

        button = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button.click()

        elem = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))
        )
        actl_feedback = elem.text
        exp_feedback = 'Correct!'

        try:
            assert actl_feedback == exp_feedback
        except AssertionError:
            self.sentence += actl_feedback
