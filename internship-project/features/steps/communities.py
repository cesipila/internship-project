from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on settings at the left side menu')
def open_settings(context):
    context.app.left_menu.open_settings()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.settings.get_current_window()


@when('Click on support option')
def click_support_option(context):
    context.app.settings.click_support()


@when('Switch to the new support tab')
def switch_to_new_window(context):
    context.app.settings.switch_to_window()


@then('Verify the support page opens')
def verify_support_page(context):
    context.app.settings.verify_support_opened()


@then('Go back to settings page')
def go_to_settings(context):
    context.app.settings.switch_window_by_id(context.original_window)


@then('Click on news option')
def click_news_option(context):
    context.app.settings.click_news()


@then('Verify the news page opens')
def verify_news_page(context):
    context.app.settings.verify_news_opened()
