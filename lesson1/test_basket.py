from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



MAIN_PAGE = "https://www.saucedemo.com/inventory.html"
BASKET_BTN = (By.ID, "shopping_cart_container")
ADD_TO_BASKET_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
ITEM_IN_BASKET = (By.ID, "item_4_title_link")
REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
EMPTY_BASKET = (By.CLASS_NAME, "cart_desc_label")
BACKPACK_ITEM = (By.ID, "item_4_title_link")
ADD_TO_CARD_IN_PRODUCT_CARD = (By.ID,"add-to-cart-sauce-labs-backpack")
# CLASS_REMOVE = (By.CLASS_NAME, "removed_cart_item")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")


def test_add_dell_product_to_basket(driver, log_in):
    driver.find_element(*ADD_TO_BASKET_BTN).click()
    driver.find_element(*BASKET_BTN).click()
    item_in_basket = driver.find_element(*ITEM_IN_BASKET).text
    assert item_in_basket == "Sauce Labs Backpack"
    driver.find_element(*REMOVE_BTN).click()
    # empty basket should have class "removed_cart_item"
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(CART_BADGE))

def test_add_dell_product_from_product_card_to_basket(driver, log_in):
    driver.find_element(*BACKPACK_ITEM).click()
    driver.find_element(*ADD_TO_CARD_IN_PRODUCT_CARD).click()
    driver.find_element(*BASKET_BTN).click()
    item_in_basket = driver.find_element(*ITEM_IN_BASKET).text
    assert item_in_basket == "Sauce Labs Backpack"
    driver.find_element(*ITEM_IN_BASKET).click()
    driver.find_element(*REMOVE_BTN).click()
    # after remove items class "shopping_cart_badge" is invisible
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(CART_BADGE))


