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
import data
from selenium.webdriver.support.ui import WebDriverWait

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

# @pytest.fixture
# def brow_options():
#     options = Options()
#     # options.add_argument('--window-size=100,100')
#     options.add_argument('--incognito')
#     options.add_argument('--headless')
#     return options


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    # user_language = request.config.getoption("language")

    options = Options()
    # options.add_experimental_option(
    #     'prefs', {'intl.accept_languages': user_language})
    # options.add_argument('--window-size=200,200')
    # options.add_argument('--start-maximized') # Maximize the browser window
    options.add_argument('--incognito')
    # options.add_argument('--disable-extensions')  # Disable Chrome extensions
    options.add_argument('--headless')
    options_firefox = OptionsFirefox()
    # options_firefox.set_preference("intl.accept_languages", user_language)
    options_edge = EdgeService()

    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # driver.maximize_window()
        # driver.implicitly_wait(15)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options_firefox)
        # driver.implicitly_wait(15)
    elif browser_name == 'edge':
        print("\nstart edge browser for test..")
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options_edge)
        # driver.implicitly_wait(15)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

# @pytest.fixture(scope="function")
# def log_in(driver):
#     driver.get(data.BASE_URL)
#     user_fild = driver.find_element(*data.USER_FILD)
#     pass_fild = driver.find_element(*data.PASSWORD_FILD)
#     user_fild.send_keys(data.LOGIN)
#     pass_fild.send_keys(data.PASSWORD)
#     driver.find_element(*data.LOGIN_BTN).click()
#     yield driver.current_url

