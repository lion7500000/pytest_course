from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_log_in_with_mouse(driver):
    action = ActionChains(driver)
    action.perform()