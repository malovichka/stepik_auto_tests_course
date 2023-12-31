import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default='chrome', 
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print('\nstart browser for testing...')
        incognito = webdriver.ChromeOptions()
        incognito.add_argument('--incognito')
        browser = webdriver.Chrome(options=incognito)
        browser.implicitly_wait(10)
    elif browser_name == 'firefox':
        print('\nstart browser for testing...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser...')
    browser.quit()
