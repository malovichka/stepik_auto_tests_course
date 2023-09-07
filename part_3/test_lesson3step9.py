from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get('http://selenium1py.pythonanywhere.com/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'button.btn')
            pytest.fail("There should be no 'Send' button")

    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get('http://selenium1py.pythonanywhere.com/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, 'no_such_button.btn')
            pytest.fail("There should be no 'Send' button")

    finally:
        browser.quit()