import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://www.w3schools.com/HTML/html5_draganddrop.asp")
driver.maximize_window()
time.sleep(1)
source=driver.find_element(By.ID,"img1")
target=driver.find_element(By.ID,"div2")

action_chains=ActionChains(driver)
action_chains.drag_and_drop(source,target).perform()
time.sleep(3)
