from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get('https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36')
    expected = 'Python String Formatting Best Practices'
    header = browser.find_element(By.TAG_NAME, 'h1')
    actual = header.text

    assert expected == actual, \
        f'Got wrong text - {actual} instead of {expected}'


finally:
    time.sleep(15)
    browser.quit()