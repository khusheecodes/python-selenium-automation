from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@then('Verify search results shown')
def verify_search_result(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
