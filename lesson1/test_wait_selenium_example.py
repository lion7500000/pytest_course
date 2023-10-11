from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


def test_load_button_without_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element(By.XPATH, "//button")
    load_content_button.click()
    # time.sleep()
    welcome_message = driver.find_element(By.XPATH, "//h2")

    assert welcome_message.text == "Welcome to the Unstable Load Site!"


def test_load_with_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element(By.XPATH, "//button")
    load_content_button.click()

    welcome_message = driver.find_element(By.XPATH, "//h2")

    # time.sleep(6)
    assert welcome_message.text == "Welcome to the Unstable Load Site!"



