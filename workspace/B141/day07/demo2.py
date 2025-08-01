import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample6.html")
driver.maximize_window()
time.sleep(2)
e=driver.find_element(By.ID,"A1") #find Element returns WebElement
e.clear()
time.sleep(2)
e.send_keys("Jaspreet")
time.sleep(3)

driver.find_element(By.ID,"A2").click()
time.sleep(3)