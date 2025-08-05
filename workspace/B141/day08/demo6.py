import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
time.sleep(3)
action_chains=ActionChains(driver)
action_chains.scroll_by_amount(0,1961).perform()
time.sleep(2)
action_chains.scroll_by_amount(0,-1961).perform()
time.sleep(4)