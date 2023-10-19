from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators_interactions import Locators
class TestBasket:
    locators = Locators()

    def test_add_dell_product_to_basket(self, driver, log_in):
        driver.find_element(*self.locators.ADD_TO_BASKET_BTN).click()
        driver.find_element(*self.locators.BASKET_BTN).click()
        item_in_basket = driver.find_element(*self.locators.ITEM_IN_BASKET).text
        assert item_in_basket == "Sauce Labs Backpack"
        driver.find_element(*self.locators.REMOVE_BTN).click()
        # empty basket should have class "removed_cart_item"
        test = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(self.locators.CART_BADGE))
        assert test is True

    def test_add_dell_product_from_product_card_to_basket(self,driver, log_in):
        driver.find_element(*self.locators.BACKPACK_ITEM).click()
        driver.find_element(*self.locators.ADD_TO_CARD_IN_PRODUCT_CARD).click()
        driver.find_element(*self.locators.BASKET_BTN).click()
        item_in_basket = driver.find_element(*self.locators.ITEM_IN_BASKET).text
        assert item_in_basket == "Sauce Labs Backpack"
        driver.find_element(*self.locators.ITEM_IN_BASKET).click()
        driver.find_element(*self.locators.REMOVE_BTN).click()
        # after remove items class "shopping_cart_badge" is invisible
        test = WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(self.locators.CART_BADGE))
        assert test is True