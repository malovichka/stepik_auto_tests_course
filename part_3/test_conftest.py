from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'

def test_guest_login(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '#login_link')
