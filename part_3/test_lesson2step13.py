import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMandatoryFields(unittest.TestCase):
    def test_send_form_with_mandatory_fields_1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get('http://suninjuly.github.io/registration1.html')
        
        first_name = browser.find_element(By.XPATH, '//label[contains(text(), "First name*")]/following::input[1]')
        first_name.send_keys('FirstName')
        last_name = browser.find_element(By.XPATH, '//label[contains(text(), "Last name*")]/following::input[1]')
        last_name.send_keys('LastName')
        email = browser.find_element(By.XPATH, '//label[contains(text(), "Email*")]/following::input[1]')
        email.send_keys('email@email.com') 
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        
        welcome_message = browser.find_element(By.TAG_NAME, 'h1')
        actual_header = welcome_message.text
        expected_header = 'Congratulations! You have successfully registered!'
        
        self.assertEqual(actual_header, expected_header, f'Expected {expected_header}, got {actual_header} instead')


    def test_send_form_with_mandatory_fields_2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get('http://suninjuly.github.io/registration2.html')
        
        first_name = browser.find_element(By.XPATH, '//label[contains(text(), "First name*")]/following::input[1]')
        first_name.send_keys('FirstName')
        last_name = browser.find_element(By.XPATH, '//label[contains(text(), "Last name*")]/following::input[1]')
        last_name.send_keys('LastName')
        email = browser.find_element(By.XPATH, '//label[contains(text(), "Email*")]/following::input[1]')
        email.send_keys('email@email.com') 
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        
        welcome_message = browser.find_element(By.TAG_NAME, 'h1')
        actual_header = welcome_message.text
        expected_header = 'Congratulations! You have successfully registered!'
        
        self.assertEqual(actual_header, expected_header, f'Expected {expected_header}, got {actual_header} instead')


if __name__ == '__main__':
    unittest.main()