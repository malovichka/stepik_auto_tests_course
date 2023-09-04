from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x:str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

#click the button
jorney_button = browser.find_element(By.CSS_SELECTOR, '.container>button')
jorney_button.click()

#wait until alert appears
time.sleep(1)

#confirm
confirm = browser.switch_to.alert
confirm.accept()

#solve captcha
x_elem = browser.find_element(By.ID, 'input_value')
x_value = x_elem.text
answer = calc(x_value)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

#this is sleep time to look at the results
time.sleep(7)