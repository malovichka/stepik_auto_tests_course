from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, 'peopleRule')
people_checked = people_radio.get_attribute('checked')
print("value of the people radio: ", people_checked)

assert people_checked is not None, "People radio is not selected by default"
assert people_checked == 'true', "People radio is not selected by default"


robots_radio = browser.find_element(By.ID, 'robotsRule')
robots_checked = robots_radio.get_attribute('checked')

assert robots_checked is None

time.sleep(11)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_disabled = submit_button.get_attribute('disabled')

assert submit_disabled == 'true', 'Submit button is enabled'
