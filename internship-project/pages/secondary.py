from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page
from time import sleep


class Secondary(Page):
    SECONDARY_MENU_URL = (By.CSS_SELECTOR, "a[href*='/secondary-listings']")
    FOR_SALE_TAG = (By.XPATH, "//div[contains(text(), 'Want to buy')]")
    FILTER_BTN = (By.CSS_SELECTOR, "div[wized*='openFiltersWindow']")
    WANT_TO_SELL = (By.CSS_SELECTOR, "div[wized*='ListingTypeSell']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized*='applyFilter']")
    WAIT_PAGE_LOAD = (By.CSS_SELECTOR, "img[class='unit-plan-image']")

    def open_secondary_page(self, timeout=10):
        self.open('https://soft.reelly.io/secondary-listings')

    def verify_secondary_url(self):
        # self.verify_partial_url('/secondary=listings')
        self.verify_url('https://soft.reelly.io/secondary-listings')

    def verify_for_sale_tags(self):
        elements = self.driver.find_elements(*self.FOR_SALE_TAG)
        assert len(elements) < 2, (f"Expected fewer than 2 elements with the text 'Want to buy', "
                                   f"but found {len(elements)}")

    def apply_filters(self, timeout=10):
        # Initial sleep to wait for Firefox page to start loading
        # sleep(3)

        # Set implicit wait
        self.driver.implicitly_wait(timeout)

        # Initial wait for Firefox page to finish loading
        # WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.WAIT_PAGE_LOAD))


        # Click the filters button
        filters_btn = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.FILTER_BTN))
        filters_btn.click()

        # Click the want to sell listing type
        listing_filter = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(self.WANT_TO_SELL))
        listing_filter.click()

        # Click the apply filter button
        apply_filter_btn = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(self.APPLY_FILTER_BTN))
        apply_filter_btn.click()

        # Reset implicit wait to default
        self.driver.implicitly_wait(0)
