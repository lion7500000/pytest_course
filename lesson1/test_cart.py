from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


IMAGE_PRODUCT = (By.ID, "item_4_img_link")
ITTEM_IN_BASKET = (By.ID, "item_4_title_link")
BASE_URL = "https://www.saucedemo.com/"
EXPECT_RESULT = "https://www.saucedemo.com/inventory-item.html?id=4"

def test_productcart_with_image(driver, log_in):
    driver.find_element(*IMAGE_PRODUCT).click()
    assert driver.current_url == EXPECT_RESULT, f'expected result {EXPECT_RESULT}, but got {driver.current_url} '
    driver.quit()

def test_productcart_with_name(driver, log_in):
    driver.find_element(*ITTEM_IN_BASKET).click()
    assert driver.current_url == EXPECT_RESULT, f'expected result {EXPECT_RESULT}, but got {driver.current_url} '
    driver.quit()