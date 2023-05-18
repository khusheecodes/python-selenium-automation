from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open amazon page')
def open_main_page(context):
    context.driver.get("https://www.amazon.com/")


@when('click on cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('verify cart is empty')
def empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
