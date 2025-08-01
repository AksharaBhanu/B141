import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample6.html")
driver.maximize_window()
time.sleep(2)
s=driver.find_element(By.ID,"A5").is_selected()
print(s) #True -- check box is selected

s=driver.find_element(By.ID,"A6").is_selected()
print(s) #False -- check box is NOT selected
