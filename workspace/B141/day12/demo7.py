import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_input_test")
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame("iframeResult")
driver.find_element(By.ID,'fname').send_keys("bhanu")
time.sleep(3)
