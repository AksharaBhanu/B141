import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
driver.maximize_window()
time.sleep(1)
button=driver.find_element(By.XPATH,"(//button[@type='submit'])[1]")
action_chains=ActionChains(driver)
action_chains.scroll_to_element(button).perform()
time.sleep(1)
button.click()
time.sleep(3)