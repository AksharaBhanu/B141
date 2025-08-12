import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample8.html")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"t1").send_keys("bhanu")
time.sleep(2)
driver.switch_to.frame("n1") #by name
driver.find_element(By.ID,"t2").send_keys("Jaspreet")
time.sleep(2)