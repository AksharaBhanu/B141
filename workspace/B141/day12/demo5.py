import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample8.html")
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame(0)
driver.find_element(By.ID,"t2").send_keys("Jaspreet")
time.sleep(1)
driver.switch_to.default_content() #exit from frame and go to main page
driver.find_element(By.ID,"t1").send_keys("bhanu")
time.sleep(2)