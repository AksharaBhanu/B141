import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample6.html")
driver.maximize_window()
time.sleep(2)
s=driver.find_element(By.ID,"A2").is_displayed()
print(s) #True -- element is visible

s=driver.find_element(By.ID,"A3").is_displayed()
print(s) #False -- element is not visible
