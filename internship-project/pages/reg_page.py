from selenium.webdriver.common.by import By
from pages.base_page import Page


class RegPage(Page):
    FULLNAME = (By.CSS_SELECTOR, "input[id='Full-Name']")
    PHONE = (By.CSS_SELECTOR, "input[id='phone2']")
    EMAIL = (By.CSS_SELECTOR, "input[id='Email-3']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='field']")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "a[wized='createaccountButtonSignup']")

    def open_registration_page(self):
        self.open('https://soft.reelly.io/sign-up')
        # calls base page method directly, passes url

    def __init__(self, driver):
        super().__init__(driver)

        # Define test data and locators
        self.inputs = {
            "fullname": ("John Doe", self.FULLNAME),
            "phone": ("2012227888", self.PHONE),
            "email": ("john@doe.com", self.EMAIL),
            "password": ("test123456", self.PASSWORD)
        }

    def registration_input(self):
        for field, (value, locator) in self.inputs.items():
            input_element = self.driver.find_element(*locator)
            input_element.clear()
            input_element.send_keys(value)

        # After setting the input, verify the fields
        self.verify_input()

    def verify_input(self):
        for field, (expected_value, locator) in self.inputs.items():
            if field == "password":
                # Skip verification for the password field due to typical restrictions
                continue

            input_element = self.driver.find_element(*locator)
            actual_value = input_element.get_attribute("value")

            assert actual_value == expected_value, f"Expected {field} '{expected_value}', but got '{actual_value}'"

    def create_account_button(self):
        self.click(*self.CREATE_ACCOUNT)
