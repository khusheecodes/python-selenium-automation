from selenium.webdriver.common.by import By
from behave import given, when, then

SIGN_HEADER = (By.XPATH, "//h1[@class ='a-spacing-small']")
EMAIL = ((By.ID, 'ap_email'))

@then('Verify Sign In page opens')
def verify_sigin_opens(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(*SIGN_HEADER).text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    assert context.driver.find_element(*EMAIL).is_displayed(), 'Email field not found'

