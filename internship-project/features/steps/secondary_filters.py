from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click sign in from the main page')
def click_sign_in(context):
    context.app.main_page.open_in_browser()


@when('Input email {email}')
def input_email(context, email):
    # context.driver.find_element(By.CSS_SELECTOR, "input[id='email-2']").send_keys(email)
    context.app.sign_in.input_email(email)


@when('Input password {password}')
def input_password(context, password):
    # context.driver.find_element(By.CSS_SELECTOR, "input[id='field']").send_keys(password)
    context.app.sign_in.input_password(password)


@when('Click continue from sign in page')
def click_continue(context):
    context.app.sign_in.sign_in_button()


@when('Click on secondary option at the left side menu')
def click_secondary_option(context):
    #context.driver.find_element(By.CSS_SELECTOR, "a[href*='/secondary-listings']").click()
    context.app.secondary.click_secondary()

@then('Verify the secondary page opens')
def verify_secondary_page(context):
    context.app.secondary.verify_secondary_url()


@when('Click the filters button')
def click_filter(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[wized*='openFiltersWindow']")

@when('Click the want to sell listing type')
def change_filter(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[wized*='ListingTypeSell']")


@when('Click the apply filter button')
def apply_filter(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[wized*='applyFilter']")

@then('Verify all cards have a for sale tag')
def verify_all_cards_tag(context):
    context.driver.find_elements(By.CSS_SELECTOR, "div[wized*='saleTagMLS']")


