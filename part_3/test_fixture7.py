import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser() -> webdriver.Chrome:
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()

class TestMainPage1():

    @pytest.mark.skip
    def test_loginlink(self, browser: webdriver.Chrome):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_basket(self, browser: webdriver.Chrome):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
    