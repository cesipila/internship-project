from selenium.webdriver.common.by import By
from pages.base_page import Page


class LeftMenu(Page):
    MAIN_MENU_URL = (By.LINK_TEXT, "Main Menu")
    OFF_PLAN_URL = (By.LINK_TEXT, "Off-plan")
    ADD_PROJECT_URL = (By.CSS_SELECTOR, "a[href*='/add-a-project']")
    SECONDARY_MENU_URL = (By.LINK_TEXT, "Secondary")
    CALENDAR_MENU_URL = (By.LINK_TEXT, "Calendar")
    REFERRAL_MENU_URL = (By.LINK_TEXT, "Referral")
    UNIVERSITY_MENU_URL = (By.LINK_TEXT, "University")
    MARKET_MENU_URL = (By.LINK_TEXT, "Market")
    SETTINGS_MENU_URL = (By.LINK_TEXT, "Settings")

    def click_main(self):
        self.click(*self.MAIN_MENU_URL)

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_URL)

    def open_add_project_url(self):
        self.click(*self.ADD_PROJECT_URL)

    def open_secondary(self):
        self.click(*self.SECONDARY_MENU_URL)

    def open_calendar(self):
        self.click(*self.CALENDAR_MENU_URL)

    def open_referral(self):
        self.click(*self.REFERRAL_MENU_URL)

    def open_university(self):
        self.click(*self.UNIVERSITY_MENU_URL)

    def open_market(self):
        self.click(*self.MARKET_MENU_URL)

    def open_settings(self):
        self.click(*self.SETTINGS_MENU_URL)