import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("http://www.google.com")
time.sleep(2)
driver.switch_to.new_window("window")
driver.get("http://www.fb.com")
time.sleep(2)
driver.quit()