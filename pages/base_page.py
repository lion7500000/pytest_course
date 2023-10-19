from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Page:
    def __init__(self, driver):
        self.driver = driver
        # self.base_url = 'https://www.amazon.com/'
        # self.base_url1= 'https://www.ebay.com/'
        self.wait = WebDriverWait(self.driver,15)
        self.actions = ActionChains(self.driver)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)


    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)