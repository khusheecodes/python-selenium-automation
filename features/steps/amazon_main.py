from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS_BTN = (By.ID, 'nav-cart')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterMoreOnAmazon a" )
CLICK_BEST_SEllERS = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers' ]")
BEST_SEllERS_LINK = (By.ID, '#zg_header a')
@given('Open amazon main page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()

@when('click on best sellers')
def click_bestsellers(context):
    context.driver.find_element(*CLICK_BEST_SEllERS).click()


#@then('Verify there are {expected_amount} links')
#def verify_link_count (context, expected_amount):
   # print(type(expected_amount))

   # expected_amount = int(expected_amount)
    #links_count = len(context.driver.find_elements(*FOOTER_LINKS))
    #print((context.driver.find_elements(*FOOTER_LINKS)))
    #print(type((context.driver.find_elements(*FOOTER_LINKS))))
    #assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'

@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    print(type(expected_amount))

    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*BEST_SEllERS_LINK))
    print((context.driver.find_elements(*BEST_SEllERS_LINK)))
    print(type((context.driver.find_elements(*BEST_SEllERS_LINK))))
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'