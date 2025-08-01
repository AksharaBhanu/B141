import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"input-username").send_keys("admin")
driver.find_element(By.ID,"input-password").send_keys("pointofsale")
driver.find_element(By.NAME,"login-button").click()
time.sleep(2)