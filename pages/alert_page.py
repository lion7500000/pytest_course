from pages.base_page import Page
from locators.locators_interactions import Locators


class AlertPage(Page):
    locator = Locators()

    def click_alert_btn(self):
        return self.element_is_clikable(self.locator.CLICK_ALERT_BTB)

    def click_alert_btn_5sec(self):
        return self.element_is_clikable(self.locator.ALERT_BUTTON_5SEC)

    def alert_wait_5sec(self):
        return self.alert_is_present()

    def alert_promt_btn(self):
        return self.element_is_clikable(self.locator.CONFIRM_BTN)

    def promt_alert_btn(self):
        return  self.element_is_clikable(self.locator.PROMT_BTN)

    def promt_text_assert(self):
        text = 'Hi my friend'
        return self.text_is_present(self.locator.PROMT_ENTERED_TXT, text)




