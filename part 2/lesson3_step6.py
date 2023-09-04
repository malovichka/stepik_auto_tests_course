from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x:str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

#open web-page
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)


#click the button
magic_button = browser.find_element(By.CLASS_NAME, 'trollface')
magic_button.click()

#switch to new tab
window_with_riddle = browser.window_handles[1]
browser.switch_to.window(window_with_riddle)

#robot captcha
x_elem = browser.find_element(By.ID, 'input_value')
answer = calc(x_elem.text)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer)

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()

time.sleep(10)