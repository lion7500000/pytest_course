from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lesson1 import locators

def test_add_dell_product_to_basket(driver, log_in):
    driver.find_element(*locators.ADD_TO_BASKET_BTN).click()
    driver.find_element(*locators.BASKET_BTN).click()
    item_in_basket = driver.find_element(*locators.ITEM_IN_BASKET).text
    assert item_in_basket == "Sauce Labs Backpack"
    driver.find_element(*locators.REMOVE_BTN).click()
    # empty basket should have class "removed_cart_item"
    test = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(locators.CART_BADGE))
    assert test is True

def test_add_dell_product_from_product_card_to_basket(driver, log_in):
    driver.find_element(*locators.BACKPACK_ITEM).click()
    driver.find_element(*locators.ADD_TO_CARD_IN_PRODUCT_CARD).click()
    driver.find_element(*locators.BASKET_BTN).click()
    item_in_basket = driver.find_element(*locators.ITEM_IN_BASKET).text
    assert item_in_basket == "Sauce Labs Backpack"
    driver.find_element(*locators.ITEM_IN_BASKET).click()
    driver.find_element(*locators.REMOVE_BTN).click()
    # after remove items class "shopping_cart_badge" is invisible
    test = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(locators.CART_BADGE))
    assert test is True



