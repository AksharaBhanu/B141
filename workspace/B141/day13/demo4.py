import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://aksharatraining.com/sample16.html")
driver.find_element(By.ID,"ok").click()
wait.until(expected_conditions.alert_is_present())
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()
