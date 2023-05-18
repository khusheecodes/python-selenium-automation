
driver.get("https://www.amazon.com/")

#Amamzon logo
driver.find_elements(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email Field
driver.find_elements(By.XPATH, "//input[@type='email']")

#Continuebutton
driver.find_elements(By.ID, 'continue')

#needhelplink
driver.find_elements(By.XPATH, "//span[@class='a-expander-prompt']")

#forfot your password
driver.find_elements(By.XPATH, "//a[@class='a-link-normal']")

#Other issues with Sign-in
driver.find_elements(By.ID, 'ap-other-signin-issues-link')

#Create your amazon account
driver.find_elements(By.ID, 'createAccountSubmit')

#Conditions of use
driver.find_elements(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

#Privacy Notice
driver.find_elements(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

