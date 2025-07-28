import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#open the browser
driver=Chrome()
#enter the url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
#enter the username
driver.find_element(By.NAME,"username").send_keys("Admin")
#enter the password
driver.find_element(By.NAME,"password").send_keys("admin123")
#click login button
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(5)