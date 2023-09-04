from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from test_functions import calc

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()
    x_elem = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_elem)
    x_value = x_elem.text
    answer = calc(x_value)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()