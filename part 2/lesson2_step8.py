from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#open web-page
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

#fill in fields:name, last name, email
first_name = browser.find_element(By.NAME, 'firstname')
first_name.send_keys('firstname')
last_name = browser.find_element(By.NAME, 'lastname')
last_name.send_keys('lastname')
email = browser.find_element(By.NAME, 'email')
email.send_keys('email@email.com')

#upload the file
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
upload = browser.find_element(By.ID, 'file')
upload.send_keys(file_path)

#press submit button
submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()


time.sleep(10)