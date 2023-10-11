import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.edge.options import Options as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
USER_FILD = (By.ID, "user-name")
PASSWORD_FILD = (By.ID, "password")
LOGIN_BTN = (By.ID, "login-button")

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'edge': webdriver.edge
}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    # user_language = request.config.getoption("language")

    options = Options()
    # options.add_experimental_option(
    #     'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    # options_firefox.set_preference("intl.accept_languages", user_language)
    options_edge = EdgeService()

    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options_firefox)
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == 'edge':
        print("\nstart firefox browser for test..")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options_edge)
        driver.maximize_window()
        driver.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture(scope="function")
def log_in(driver):
    driver.get(BASE_URL)
    user_fild = driver.find_element(*USER_FILD)
    pass_fild = driver.find_element(*PASSWORD_FILD)
    user_fild.send_keys("standard_user")
    pass_fild.send_keys("secret_sauce")
    driver.find_element(*LOGIN_BTN).click()
    yield driver.current_url

# @pytest.fixture(scope='session')
# def driver():
#     print('\nstart browser...')
#     chrome_options = Options()
#     if 'CI' in os.environ:
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         driver.maximize_window()
#     else:
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.maximize_window()
#     yield driver
#     print('\nquit browser...')
#     driver.quit()

