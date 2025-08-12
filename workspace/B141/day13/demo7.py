import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#NoSuchElementException
#solution1--implicitly wait
#solution2--time sleep
driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
