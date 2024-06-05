from selenium.common import NoSuchElementException
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


@when('Input email {email} and pwd {password}')
def input_login(context, email, password):
    context.app.sign_in.input_login(email, password)


@when('Click continue from sign in page')
def click_continue(context):
    context.app.sign_in.sign_in_button()


@when('Click on secondary option at the left side menu')
def click_secondary_option(context):
    context.app.left_menu.open_secondary()


@when('Verify the secondary page opens')
def verify_secondary_page(context):
    context.app.secondary.verify_secondary_url()


@when('Filter the products by want to sell')
def filter_products_by_to_sell(context):
    context.app.secondary.apply_filters()


@then('Verify all cards have a for sale tag')
def verify_all_cards_tag(context):
    context.app.secondary.verify_for_sale_tags()
