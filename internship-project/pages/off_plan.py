from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class OffPlan(Page):
    OFF_PLAN_PAGE_CHECK = (By.CSS_SELECTOR, "div[class*='page-title off_plan']")
    FILTER_BY_PRICE_FROM = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    FILTER_BY_PRICE_TO = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    PRICE_ON_CARDS = (By.CSS_SELECTOR, "div[wized='projectMinimumPrice']")

    def verify_off_plan_header(self, timeout=10):
        # Wait until the element is present and visible
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.OFF_PLAN_PAGE_CHECK))

        # Verify the text in the element
        assert 'Total projects' in element.text, f"Expected text 'Total projects' not found in {element.text}"

    def set_price_range(self, from_price, to_price, timeout=10):
        # Wait until the "from price" input field is visible and interactable
        price_from_input = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.FILTER_BY_PRICE_FROM)
        )
        price_from_input.clear()
        price_from_input.send_keys(from_price)

        # Wait until the "to price" input field is visible and interactable
        price_to_input = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.FILTER_BY_PRICE_TO)
        )
        price_to_input.clear()
        price_to_input.send_keys(to_price)

    def verify_prices_in_range(self, min_price, max_price, timeout=10):
        # convert min_price and max_price to integers
        min_price = int(min_price)
        max_price = int(max_price)

        # Wait until the price elements are present
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(self.PRICE_ON_CARDS))

        # Find all price elements
        price_elements = self.driver.find_elements(*self.PRICE_ON_CARDS)

        # verify the prices
        for price_element in price_elements:
            price_text = price_element.text
            price_value = int(price_text.replace("AED", "").replace(",", "").strip())

            # Assert that the price is within the range
            assert min_price <= price_value <= max_price, f"Price {price_value} is outside the range ({min_price}-{max_price})"
            print(f"Price {price_value} is within the range.")
