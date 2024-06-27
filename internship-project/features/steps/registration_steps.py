from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the registration page')
def open_registration_page(context):
    context.app.reg_page.open_registration_page()


@when('Enter some information in the input fields')
def registration_input(context):
    context.app.reg_page.registration_input()


@then('Verify the right information is present')
def verify_input(context):
    context.app.reg_page.verify_input()
