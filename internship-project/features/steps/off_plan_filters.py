from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on off plan at the left side menu')
def click_off_plan_left_side_menu(context):
    context.app.left_menu.click_off_plan()


@when('Verify the right page opens')
def verify_right_page(context):
    context.app.off_plan.verify_off_plan_header()
    sleep(3)  # page refresh takes awhile then impacts next step


@when('Click the off-plan filters button')
def click_off_plan_filters_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[wized='openFiltersWindow']"
                                                 "[class='filter-button w-inline-block']").click()


@when('Set the range from {from_price} to {to_price}')
def set_price_range(context, from_price, to_price):
    context.app.off_plan.set_price_range(from_price, to_price)


@when('Click the off-plan apply filter button')
def click_off_plan_apply_filter_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[wized='applyFilterButton']").click()
    sleep(10)


@then('Verify the price in all cards is within {min_price} to {max_price} range')
def verify_price_range(context, min_price, max_price):
    context.app.off_plan.verify_prices_in_range(min_price, max_price)
