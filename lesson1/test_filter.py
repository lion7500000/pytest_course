from selenium.webdriver.common.by import By


MAIN_PAGE = "https://www.saucedemo.com/inventory.html"
CART_ITEMS_TEXT = (By.CSS_SELECTOR,".inventory_list .inventory_item_name")
CART_ITEMS_PRICE = (By.CSS_SELECTOR,".inventory_list .inventory_item_price")
FILTER_AZ = (By.CSS_SELECTOR, ".product_sort_container option[value='az']")
FILTER_ZA = (By.CSS_SELECTOR, ".product_sort_container option[value='za']")
FILTER_LOW_HIGH = (By.CSS_SELECTOR, ".product_sort_container option[value='lohi']")
FILTER_HIGH_LOW = (By.CSS_SELECTOR, ".product_sort_container option[value='hilo']")


def test_itema_AZ(driver, log_in):
    #set filter fom a to z
    driver.find_element(*FILTER_AZ).click()
    items = driver.find_elements(*CART_ITEMS_TEXT)
    expect_cart_items_AZ= ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '


def test_items_ZA(driver, log_in):
    #set filter fom z to a
    driver.find_element(*FILTER_ZA).click()
    items = driver.find_elements(*CART_ITEMS_TEXT)
    expect_cart_items_AZ = ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']
    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '

def test_items_low_price(driver, log_in):
    # set filter fom low to high
    driver.find_element(*FILTER_LOW_HIGH).click()
    items = driver.find_elements(*CART_ITEMS_PRICE)
    expect_cart_items_AZ = ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']

    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '

def test_items_high_price(driver, log_in):
    # set filter fom High to low
    driver.find_element(*FILTER_HIGH_LOW).click()
    items = driver.find_elements(*CART_ITEMS_PRICE)
    expect_cart_items_AZ = ['$49.99', '$29.99', '$15.99', '$15.99', '$9.99', '$7.99']

    actual_cart_item = []
    for item in items:
        actual_cart_item.append(item.text)
    assert actual_cart_item == expect_cart_items_AZ, f'expected result {expect_cart_items_AZ}, but got {actual_cart_item} '





