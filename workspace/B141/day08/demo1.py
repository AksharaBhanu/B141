import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
driver.find_element(By.ID,"input-username").screenshot('username.png')
driver.find_element(By.NAME,'login-button').screenshot('gobutton.png')
driver.quit()

