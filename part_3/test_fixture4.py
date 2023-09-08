import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='class')
def browser():
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()


class TestMainPage1():
    def test_login_link(self, browser):
        print('start test 1')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('finish test1')

    def test_basket(self, browser):
        print('start test2')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")