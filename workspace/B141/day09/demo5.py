import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample15.html")
all_checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in all_checkbox:
    checkbox.click()

time.sleep(2)

for checkbox in reversed(all_checkbox):
    checkbox.click()

time.sleep(2)