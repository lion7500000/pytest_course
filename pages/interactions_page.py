from pages.base_page import Page
from locators.locators_interactions import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By


class InteractionPage(Page):
    locator = Locators()

    def inter_drag_drop(self):
        drag1 = self.element_is_visible(self.locator.DRAG)
        drop1 = self.element_is_visible(self.locator.DROP)
        self.drag_and_drop(drag1, drop1)
        text = self.element_is_visible(self.locator.TEXT_DROPPED).text
        return text

    def accept_drag_drop(self):
        self.element_is_visible(self.locator.ACCEPT_MENU).click()
        #
        drag1 = self.element_is_visible(self.locator.ACCEPT_DROP)
        # drop = self.element_is_visible(self.locator.ACCEPT_DROP)
        # self.drag_and_drop(drag1, drop)
        # # drag2 = self.element_is_visible(self.locator.NOT_ACCEPT_DRAG)
        # self.drag_and_drop(drag2, drop)
        # text = self.element_is_visible(self.locator.ACCEPT_DROP_TEXT).text
        # return text




