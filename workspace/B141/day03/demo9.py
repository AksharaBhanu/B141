import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()

driver.get("https://pos.aksharatraining.in/pos/public/")

driver.find_element(By.CSS_SELECTOR,"input[id='input-username']").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"input[id='input-password']").send_keys("pointofsale")
driver.find_element(By.CSS_SELECTOR,"button[name='login-button']").click()
time.sleep(2)