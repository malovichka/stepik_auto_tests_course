from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # my code
    #elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    #for element in elements:
        #element.send_keys('123')
    #end of my old code

    first_name = browser.find_element(By.XPATH, '//label[contains(text(), "First name*")]/following::input[1]')
    first_name.send_keys('FirstName')
    last_name = browser.find_element(By.XPATH, '//label[contains(text(), "Last name*")]/following::input[1]')
    last_name.send_keys('LastName')
    email = browser.find_element(By.XPATH, '//label[contains(text(), "Email*")]/following::input[1]')
    email.send_keys('email@email.com') 


    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_text_elt.text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    