from pages.base_page import Page
from locators.locators_interactions import Locators


class RegistrationPage(Page):

    locator = Locators()

    def test_registration(self):

        hesder = self.element_is_visible(self.locator.HEADER_TEXT)
        assert hesder.text == "Практика с ожиданиями в Selenium"
        start = self.element_is_visible(self.locator.START_BUTTON)
        start.click()
        log_in = self.input_text('test@gmail.com',self.locator.LOG_FILD)
        password = self.input_text("test", self.locator.PASS_FILD)
        check_box = self.element_is_visible(self.locator.AGREE_CHECK_BOX)
        check_box.click()
        assert check_box.is_selected() == True
        button = self.element_is_visible(self.locator.REG_BTN)
        button.click()
        text = self.element_is_visible(self.locator.SUCCESS_TEXT)
        return text.text



