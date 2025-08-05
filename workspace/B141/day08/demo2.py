import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/")
time.sleep(1)
driver.save_screenshot('loginpage.png')
time.sleep(1)
driver.quit()