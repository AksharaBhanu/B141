import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#NoSuchElementException
#solution1--implicitly wait
#solution2--time sleep
#solution3-WebDriverWait
driver=Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
t=(By.XPATH,"//input[@name='username']")
wait.until(expected_conditions.visibility_of_element_located(t))
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
