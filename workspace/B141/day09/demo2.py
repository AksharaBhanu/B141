import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample2.html")
time.sleep(1)
all_elements=driver.find_elements(By.TAG_NAME,"a")
for element in all_elements:
    print(element.get_attribute('href'))