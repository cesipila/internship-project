from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Secondary(Page):
    SECONDARY_MENU_URL = (By.CSS_SELECTOR, "a[href*='/secondary-listings']")

    def open_secondary_page(self):
        self.open('https://soft.reelly.io/secondary-listings')
        # calls base page method directly, passes url

    def verify_secondary_url(self):
        # self.verify_partial_url('terms-conditions/')
        self.verify_url('https://soft.reelly.io/secondary-listings')


    def click_secondary(self):
        self.click(*self.SECONDARY_MENU_URL)


