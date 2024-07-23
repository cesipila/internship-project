from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    OPEN_IN_BROWSER = (By.CSS_SELECTOR, "div[class*='text-block-36']")
    CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "div[class='get-free-period menu")

    def open_main_page(self):
        self.open('https://www.reelly.io/')
        # calls base page method directly, passes url


    def open_in_browser(self):
        self.click(*self.OPEN_IN_BROWSER)
        # sign in button from the main page

    def connect_the_company (self):
        self.click(*self.CONNECT_THE_COMPANY)
        # sign in button from the main page

