from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):
    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "input[id='email-2']")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "input[id='field']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def input_login(self, email, password):
        email_input = self.driver.find_element(*self.SIGN_IN_EMAIL)
        email_input.clear()
        email_input.send_keys(email)

        pwd_input = self.find_element(*self.SIGN_IN_PASSWORD)
        pwd_input.clear()
        pwd_input.send_keys(password)

    def sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)
