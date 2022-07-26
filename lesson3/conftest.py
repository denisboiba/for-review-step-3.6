import pytest
from selenium import webdriver


def pytest_addoption(parser):  # pytest_addoption - Встроенная ф-я, parser - атрибут объекта request
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    # default=None - параметр 'browser_name' обязательный, ксли не указать -> Error
    # default='chrome' -  chrome будет по деф-у и тогда параметр 'browser_name' не будет обязательным


@pytest.fixture(scope="function")
def browser(request):  # request -  Встроенная фикстура для анализа контекста запрашивающей тестовой ф-и/cls/модуля
    browser_name = request.config.getoption("browser_name")  # инициал-я в cmd запроса значения
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
