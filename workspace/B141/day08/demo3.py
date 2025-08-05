import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
time.sleep(4)
driver.save_screenshot('contact.png')
time.sleep(1)
driver.quit()