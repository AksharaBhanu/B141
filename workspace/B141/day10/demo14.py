import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


#download the file
driver=Chrome()
driver.get("https://aksharatraining.com/sample7.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"A3").click()
time.sleep(3)