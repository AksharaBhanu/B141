import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample6.html")
driver.maximize_window()
time.sleep(2)
s=driver.find_element(By.ID,"A1").is_enabled()
print(s) #True -- element is enabled

s=driver.find_element(By.ID,"A4").is_enabled()
print(s) #False -- element is disabled
