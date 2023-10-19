from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lesson1 import locators


def test_menu_log_out(driver, log_in):
    #click to hamburger menu
    driver.find_element(*locators.HAMBUR_MENU).click()
    #click to log_out mrnu
    driver.find_element(*locators.HAM_LOG_OUT).click()
    assert driver.current_url == locators.LOG_IN_URL

def test_menu_about (driver, log_in):
    # click to hamburger menu
    driver.find_element(*locators.HAMBUR_MENU).click()
    # click to about menu
    driver.find_element(*locators.HAM_ABOUT_MNU).click()
    assert driver.current_url == locators.ABOUT_URL

def test_reset_app_state(driver, log_in):
    # click to hamburger menu
    driver.find_element(*locators.HAMBUR_MENU).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.HAM_RESET_APP_STATE))





