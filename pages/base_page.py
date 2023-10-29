from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
from locators.locators_interactions import Locators
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




class Page:

    locator = Locators
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        # self.base_url = 'https://www.amazon.com/'
        # self.base_url1= 'https://www.ebay.com/'
        self.wait = wait(self.driver, 25)
        self.actions = ActionChains(self.driver)

    def open_browser(self):
        self.driver.get(self.url)


    def click_menu(self,locator):
        self.driver.find_element(locator).click()

    def input_text(self, text, locator):
        e = self.driver.find_element(locator)
        e.clear()
        e.send_keys(text)


    def find_element(self,locator):
        return self.driver.find_element(locator)


    def find_element_text(self, *locator):
        return self.driver.find_element(*locator).text()

    def find_elements(self,locator):
        return self.driver.find_elements(locator)

    def drag_and_drop(self, drag, drop):
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()

    def element_is_clikable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))