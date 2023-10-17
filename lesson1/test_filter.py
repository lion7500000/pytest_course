import locators

def test_itema_AZ(driver, log_in):
    #set filter fom a to z
    driver.find_element(*locators.FILTER_AZ).click()
    items = driver.find_elements(*locators.CART_ITEMS_TEXT)
    expect_cart_items_AZ= ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '


def test_items_ZA(driver, log_in):
    #set filter fom z to a
    driver.find_element(*locators.FILTER_ZA).click()
    items = driver.find_elements(*locators.CART_ITEMS_TEXT)
    expect_cart_items_AZ = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '

def test_items_low_price(driver, log_in):
    # set filter fom low to high
    driver.find_element(*locators.FILTER_LOW_HIGH).click()
    items = driver.find_elements(*locators.CART_ITEMS_PRICE)
    expect_cart_items_AZ = ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']

    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '

def test_items_high_price(driver, log_in):
    # set filter fom High to low
    driver.find_element(*locators.FILTER_HIGH_LOW).click()
    items = driver.find_elements(*locators.CART_ITEMS_PRICE)
    expect_cart_items_AZ = ['$49.99', '$29.99', '$15.99', '$15.99', '$9.99', '$7.99']

    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '





