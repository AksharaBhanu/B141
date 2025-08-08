import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']").click()
time.sleep(4)
all_tabs=driver.window_handles
driver.switch_to.window(all_tabs[1]) #switch to 2nd tab
driver.find_element(By.ID,"Form_submitForm_action_request").click()
time.sleep(3)



