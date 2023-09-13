import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser() -> webdriver.Chrome:
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nclose browser...')
    browser.quit()


class TestMainPage1():

    def test_loginlnk(self, browser: webdriver.Chrome):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_basket(self, browser: webdriver.Chrome):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail(reason='for learning purposes')
    def test_guest_search(self, browser:webdriver.Chrome):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'input.btn.btn-default')