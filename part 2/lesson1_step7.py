from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

# find image with treasure chest
# get x - valuex attribute
treasure_chest = browser.find_element(By.ID, 'treasure')
x_value = treasure_chest.get_attribute('valuex')

# get calc(x)
y_value = calc(x_value)

# put result
answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(y_value)

# check robot checkbox
robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

# robot radiobutton
robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
robot_radiobutton.click()

# submit
submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

time.sleep(10)