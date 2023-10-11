from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

HAMBUR_MENU = (By.ID, "react-burger-menu-btn")
HAM_LOG_OUT = (By.ID, "logout_sidebar_link")
LOG_IN_URL = "https://www.saucedemo.com/"
HAM_ABOUT_MNU = (By.ID, "about_sidebar_link")
ABOUT_URL = "https://saucelabs.com/"
HAM_RESET_APP_STATE = (By.ID, "reset_sidebar_link")

def test_menu_log_out(driver, log_in):
    #click to hamburger menu
    driver.find_element(*HAMBUR_MENU).click()
    #click to log_out mrnu
    driver.find_element(*HAM_LOG_OUT).click()
    assert driver.current_url == LOG_IN_URL

def test_menu_about (driver, log_in):
    # click to hamburger menu
    driver.find_element(*HAMBUR_MENU).click()
    # click to about menu
    driver.find_element(*HAM_ABOUT_MNU).click()
    assert driver.current_url == ABOUT_URL

def test_reset_app_state(driver, log_in):
    # click to hamburger menu
    driver.find_element(*HAMBUR_MENU).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HAM_RESET_APP_STATE))





