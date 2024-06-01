from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from time import sleep


class Settings(Page):
    EDIT_PROFILE_URL = (By.LINK_TEXT, "Edit profile")
    CALENDAR_URL = (By.LINK_TEXT, "Calendar")
    ADD_PROJECT_URL = (By.LINK_TEXT, "Add a project")
    SUPPORT_URL = (By.LINK_TEXT, "Support")
    NEWS_URL = (By.LINK_TEXT, "News")
    COMMUNITY_URL = (By.LINK_TEXT, "Community")
    CONTACT_US_URL = (By.LINK_TEXT, "Contact us")
    USER_GUIDE_URL = (By.LINK_TEXT, "User guide")
    VERIFICATION_URL = (By.LINK_TEXT, "Verification")
    CHANGE_PWD_URL = (By.LINK_TEXT, "Verification")
    SUBSCRIPTIONS_PAYMENTS_URL = (By.LINK_TEXT, "Subscription & payments")
    LOG_OUT_URL = (By.LINK_TEXT, "Log out")

    def click_edit_profile(self):
        self.click(*self.EDIT_PROFILE_URL)

    def click_calendar(self):
        self.click(*self.CALENDAR_URL)

    def click_add_project_url(self):
        self.click(*self.ADD_PROJECT_URL)

    def click_support(self):
        self.click(*self.SUPPORT_URL)

    def click_news(self):
        self.click(*self.NEWS_URL)

    def verify_support_opened(self):
        self.verify_partial_url('https://api.whatsapp.com/send?phone=')

    def verify_news_opened(self):
        self.verify_partial_url('https://t.me/reellydxb')
