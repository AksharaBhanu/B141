import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
time.sleep(3)
action_chains=ActionChains(driver)
for i in range(4):
    action_chains.scroll_by_amount(0,300).perform()
    time.sleep(1)

for i in range(4):
    action_chains.scroll_by_amount(0,-300).perform()
    time.sleep(1)

time.sleep(4)