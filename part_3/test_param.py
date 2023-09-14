import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ['ru', 'en-GB'])
def test_loginlink(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#login_link')

@pytest.mark.parametrize('language', ['ru', 'en-GB'])
class TestLogin:

    def test_guest_loginlink(self, browser, language):
        link = f'http://selenium1py.pythonanywhere.com/{language}/'
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')