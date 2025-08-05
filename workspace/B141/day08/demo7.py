import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
time.sleep(3)
element=driver.find_element(By.XPATH,"//h5[contains(text(),'All rights reserved')]")
action_chains=ActionChains(driver)
action_chains.scroll_to_element(element).perform()
time.sleep(3)