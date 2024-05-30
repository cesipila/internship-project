from selenium.webdriver.common.by import By
from pages.base_page import Page


class OffPlan(Page):
    OFF_PLAN_PAGE_CHECK = (By.CSS_SELECTOR, "div[class*='page-title off_plan']")
    FILTER_BY_PRICE_FROM = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    FILTER_BY_PRICE_TO = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    PRICE_ON_CARDS = (By.CSS_SELECTOR, "div[wized='projectMinimumPrice']")

    def verify_off_plan_header(self):
        self.verify_text('Total projects', *self.OFF_PLAN_PAGE_CHECK)

    def set_price_range(self, from_price, to_price):
        price_input = self.driver.find_element(*self.FILTER_BY_PRICE_FROM)
        price_input.clear()
        price_input.send_keys(from_price)

        price_input = self.driver.find_element(*self.FILTER_BY_PRICE_TO)
        price_input.clear()
        price_input.send_keys(to_price)

    def verify_prices_in_range(self, min_price, max_price):
        # convert min_price and max_price to integers
        min_price = int(min_price)
        max_price = int(max_price)

        price_elements = self.driver.find_elements(*self.PRICE_ON_CARDS)

        # verify the prices
        for price_element in price_elements:
            price_text = price_element.text
            price_value = int(price_text.replace("AED", "").replace(",", "").strip())

            # Assert that the price is within the range
            assert min_price <= price_value <= max_price, f"Price {price_value} is outside the range ({min_price}-{max_price})"
            print(f"Price {price_value} is within the range.")
