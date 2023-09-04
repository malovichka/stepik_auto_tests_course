from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


# open the web-page
link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

#find the x element
x_element = browser.find_element(By.ID, 'input_value')

#retrieve value for the x element
x_value = x_element.text

#calculate y value with calc function defined in the top of the test
y_value = calc(x_value)

#find input field for the answer and put the answer
answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(y_value)

#check the checkbox
robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

#select radiobutton
robot_radiobutton = browser.find_element(By.ID, 'robotsRule')
robot_radiobutton.click()

#click submit
submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()