from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click sign in from the registration page')
def click_continue(context):
    context.app.reg_page.sign_in()


@when('Click on Connect the company')
def click_connect_company(context):
    context.app.main_page.connect_the_company()


@then('Verify the correct tab opens')
def step_verify_correct_tab(context):
    context.app.settings.verify_connect_opened()
