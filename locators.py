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


driver.get("https://www.amazon.com/")

#By ID
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click()

#By Xpath
driver.find_elements(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_elements(By.XPATH, "//input[@aria-label='Search Amazon']")

#By xpath multiple attributes
driver.find_element(By.XPATH, "//input[@autocomplete='off' and @dir='auto' ]")
driver.find_element(By.XPATH, "//input[@autocomplete='off' and @tabindex='0' ]")

#By xpath text
driver.find_element(By.XPATH,"//a[text(), 'Best Sell')]")

#By Xpath, contains
driver.find_element(By.XPATH,"//a[contains[text(), 'Best Sell')]")

#By Xpath, from parent to child

driver.find_element(By.XPATH, "//div[@id= 'nav-shop-container']//a[text()='Best Seller']")


