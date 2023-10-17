import locators

def test_productcart_with_image(driver, log_in):
    driver.find_element(*locators.IMAGE_PRODUCT).click()
    assert driver.current_url == locators.EXPECT_RESULT, f'expected result {locators.EXPECT_RESULT}, but got {driver.current_url} '
    driver.quit()

def test_productcart_with_name(driver, log_in):
    driver.find_element(*locators.ITTEM_IN_BASKET).click()
    assert driver.current_url == locators.EXPECT_RESULT, f'expected result {locators.EXPECT_RESULT}, but got {driver.current_url} '
    driver.quit()