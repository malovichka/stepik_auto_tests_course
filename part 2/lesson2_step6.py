from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

# open web-page
link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

# get x value
x_elem = browser.find_element(By.ID, 'input_value')
x_value = x_elem.text

# get value of calc(x)
answer = calc(x_value)

# scroll page down
# put the answer in the field
answer_field = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
answer_field.send_keys(answer)

# check robot checkbox
robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

# check robot radiobutton
robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
robot_radiobutton.click()

# click submit
submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

time.sleep(10)