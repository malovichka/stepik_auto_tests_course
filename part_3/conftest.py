import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser() -> webdriver.Chrome:
    print('\nstart browser for testing...')
    incognito = webdriver.ChromeOptions()
    incognito.add_argument('--incognito')
    browser = webdriver.Chrome(options=incognito)
    browser.implicitly_wait(10)
    yield browser
    print('\nquit browser...')
    browser.quit()