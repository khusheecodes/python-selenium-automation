from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon image
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Your Name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Your Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-content')

#Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Continue/ Create your Amazon account
driver.find_element(By.CSS_SELECTOR, '#continue')

#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#signin
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')