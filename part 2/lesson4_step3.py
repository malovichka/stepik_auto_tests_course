from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/wait1.html')


verify_button = browser.find_element(By.ID, 'verify')
verify_button.click()

verification = browser.find_element(By.ID, 'verify_message')
verification_message = verification.text

assert 'Verification was successful!' == verification_message

# or this will also work (and then we don't need line 12)
assert 'successful' in verification.text