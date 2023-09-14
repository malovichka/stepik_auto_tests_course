from selenium.webdriver.common.by import By
import pytest
import time
import math

urls = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', urls)
def test_login(browser, link):
    try:
        browser.get(link)
        auth_button = browser.find_element(By.CLASS_NAME, 'navbar__auth_login')
        auth_button.click()

        auth_login = browser.find_element(By.ID, 'id_login_email')
        auth_login.send_keys('###')
        auth_password = browser.find_element(By.ID, 'id_login_password')
        auth_password.send_keys('###')
        auth_submit = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
        auth_submit.click()


        print('trying to find the submission form')
        time.sleep(2)
        answer_field = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        answer = str(math.log(int(time.time() + 0.2)))
        print(answer)
        answer_field.send_keys(answer)

        print('submitting the answer')
        submit_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit_button.click()

        message_element = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        actual = message_element.text
        expected = 'Correct!'

        assert actual == expected, f'Expected **{expected}**, got **{actual}** instead'

    finally:
       reset_button = browser.find_element(By.CLASS_NAME, 'again-btn')
       reset_button.click()








    