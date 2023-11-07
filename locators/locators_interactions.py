from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    # test_basket
    MAIN_PAGE = "https://www.saucedemo.com/inventory.html"
    BASKET_BTN = (By.ID, "shopping_cart_container")
    ADD_TO_BASKET_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    ITEM_IN_BASKET = (By.ID, "item_4_title_link")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    EMPTY_BASKET = (By.CLASS_NAME, "cart_desc_label")
    BACKPACK_ITEM = (By.ID, "item_4_title_link")
    ADD_TO_CARD_IN_PRODUCT_CARD = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # logIn
    ERROR_MES = (By.CSS_SELECTOR, ".error-message-container.error")
    ERROR_TXT = 'Epic sadface: Username and password do not match any user in this service'

    # Ham menu
    HAMBUR_MENU = (By.ID, "react-burger-menu-btn")
    HAM_LOG_OUT = (By.ID, "logout_sidebar_link")
    LOG_IN_URL = "https://www.saucedemo.com/"
    HAM_ABOUT_MNU = (By.ID, "about_sidebar_link")
    ABOUT_URL = "https://saucelabs.com/"
    HAM_RESET_APP_STATE = (By.ID, "reset_sidebar_link")

    # cart
    IMAGE_PRODUCT = (By.ID, "item_4_img_link")
    ITTEM_IN_BASKET = (By.ID, "item_4_title_link")
    EXPECT_RESULT = "https://www.saucedemo.com/inventory-item.html?id=4"

    # filter
    CART_ITEMS_TEXT = (By.CSS_SELECTOR, ".inventory_list .inventory_item_name")
    CART_ITEMS_PRICE = (By.CSS_SELECTOR, ".inventory_list .inventory_item_price")
    FILTER_AZ = (By.CSS_SELECTOR, ".product_sort_container option[value='az']")
    FILTER_ZA = (By.CSS_SELECTOR, ".product_sort_container option[value='za']")
    FILTER_LOW_HIGH = (By.CSS_SELECTOR, ".product_sort_container option[value='lohi']")
    FILTER_HIGH_LOW = (By.CSS_SELECTOR, ".product_sort_container option[value='hilo']")

    # irder the product
    CHECKOUT_BTN = (By.CSS_SELECTOR, "button#checkout")
    FIRST_NAME_FILD = (By.ID, "first-name")
    LAST_NAME_FILD = (By.ID, "last-name")
    ZIP_COD_FILD = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    CHECKOUT_TEXT = (By.CSS_SELECTOR, ".title")
    CHECKOUT_OVERVIEW = (By.CSS_SELECTOR, "span.title")
    FINISH_BTN = (By.CSS_SELECTOR, "button#finish")
    CHECKOUT_COMPLETE_TEXT = (By.CSS_SELECTOR, "span.title")

    # drag and drop site
    DRAG = (By.CSS_SELECTOR, "#simpleDropContainer div[id='draggable']")
    DROP = (By.CSS_SELECTOR, "#simpleDropContainer div[id='droppable']")
    TEXT_DROPPED = (By.CSS_SELECTOR, "#simpleDropContainer div[id='droppable'] p")
    ACCEPT_MENU = (By.CSS_SELECTOR, '#droppableExample-tab-accept')
    ACCEPT_DRAG = (By.ID, 'acceptable')
    NOT_ACCEPT_DRAG = (By.ID, 'notAcceptable')
    ACCEPT_DROP = (By.CSS_SELECTOR, '#droppable')
    ACCEPT_DROP_TEXT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable p')

    #registration page from Vic
    HEADER_TEXT = (By.XPATH, '//h1')
    START_BUTTON = (By.ID, 'startTest')
    LOG_FILD = (By.CSS_SELECTOR, '#registrationForm #login')
    PASS_FILD = (By.CSS_SELECTOR, '#registrationForm #password')
    AGREE_CHECK_BOX = (By.XPATH, "//input[@id='agree']")
    REG_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")
    SUCCESS_TEXT = (By.ID, 'successMessage')

    # alert
    CLICK_ALERT_BTB = (By.XPATH, '//button[@id="alertButton"]')
    ALERT_BUTTON_5SEC = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BTN = (By.XPATH, '//button[@id="confirmButton"]')
    PROMT_BTN = (By.XPATH, '//button[@id="promtButton"]')
    PROMT_ENTERED_TXT = (By.XPATH, '//span[@id="promptResult"]')
