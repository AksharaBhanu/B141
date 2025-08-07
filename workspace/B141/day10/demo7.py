import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample7.html")
time.sleep(1)
driver.find_element(By.ID,"A1").click()
time.sleep(1)
alert=driver.switch_to.alert #goto alert
print(alert.text)
alert.dismiss()
time.sleep(1)
print(driver.find_element(By.ID,"message").text)

