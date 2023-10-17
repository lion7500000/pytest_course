import locators
import data
def test_order_product(log_in, driver):
    driver.find_element(*locators.ADD_TO_BASKET_BTN).click()
    driver.find_element(*locators.BASKET_BTN).click()
    item_in_basket = driver.find_element(*locators.ITEM_IN_BASKET).text
    assert item_in_basket == "Sauce Labs Backpack"
    driver.find_element(*locators.CHECKOUT_BTN).click()
    expect_text = driver.find_element(*locators.CHECKOUT_TEXT).text
    assert  expect_text == data.CHECK_OUT_TXT, f'Expected result {data.CHECK_OUT_TXT}, but got {expect_text}'
    driver.find_element(*locators.FIRST_NAME_FILD).send_keys(data.FIRST_NAME)
    driver.find_element(*locators.LAST_NAME_FILD).send_keys(data.LAST_NAME)
    driver.find_element(*locators.ZIP_COD_FILD).send_keys(data.ZIP_COD)
    driver.find_element(*locators.CONTINUE_BTN).click()
    expect_text2 = driver.find_element(*locators.CHECKOUT_OVERVIEW).text
    assert expect_text2 == data.CHECK_OUT_TXT2, f'Expected result {data.CHECK_OUT_TXT2}, but got {expect_text2}'
    driver.find_element(*locators.FINISH_BTN).click()
    expect_text3 = driver.find_element(*locators.CHECKOUT_COMPLETE_TEXT).text
    assert expect_text3 == data.CHECK_OUT_COMP_TXT, f'Expected result {data.CHECK_OUT_COMP_TXT}, but got {expect_text3}'