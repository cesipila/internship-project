from pages.left_menu import LeftMenu
from pages.off_plan import OffPlan
from pages.base_page import Page
from pages.reg_page import RegPage
from pages.settings import Settings
from pages.sign_in import SignIn
from pages.main_page import MainPage
from pages.secondary import Secondary


class Application:

    def __init__(self, driver):
        self.left_menu = LeftMenu(driver)
        self.off_plan = OffPlan(driver)
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.reg_page = RegPage(driver)
        self.settings = Settings(driver)
        self.sign_in = SignIn(driver)
        self.secondary = Secondary(driver)
