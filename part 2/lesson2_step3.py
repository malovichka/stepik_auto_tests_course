from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

#def first_second_sum(first: str, second: str) -> str:
#    result = int(first) + int(second)
#    return str(result)

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

first_element = browser.find_element(By.ID, 'num1')
first_value = first_element.text
second_element = browser.find_element(By.ID, 'num2')
second_value = second_element.text

addition = lambda x, y: str(int(x) + int(y))
answer = addition(first_value, second_value)

dropdown_with_answers = Select(browser.find_element(By.TAG_NAME, 'select'))
dropdown_with_answers.select_by_value(answer)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

time.sleep(10)