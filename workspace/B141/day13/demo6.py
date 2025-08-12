import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#NoSuchElementException
#solution1--implicitly wait
driver=Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
