import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# scenario --login to POS application
#steps
#1-open the browser
driver=Chrome()
#2-enter the url
driver.get("https://pos.aksharatraining.in/pos/public/")
#3-enter the username as admin
driver.find_element(By.ID,"input-username").send_keys("admin")
#4-enter the password as pointofsale
driver.find_element(By.ID,"input-password").send_keys("pointofsale")
#5-click on go button
driver.find_element(By.NAME,"login-button").click()
time.sleep(3)