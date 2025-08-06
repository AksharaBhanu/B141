import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,'APjFqb').send_keys("selenium")
time.sleep(2)
all_auto_suggestions=driver.find_elements(By.XPATH,"//span[contains(text(),'selenium')]")
for suggestion in all_auto_suggestions:
    print(suggestion.text)
