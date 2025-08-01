import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample6.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"A5").click()
time.sleep(2)
driver.find_element(By.ID,"A5").click()
time.sleep(2)