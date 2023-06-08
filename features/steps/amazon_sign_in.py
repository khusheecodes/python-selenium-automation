from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open amazon search page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('click on return and orders')
def click_return_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('verify users see signin')
def verify_sigin(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class ='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not found'
