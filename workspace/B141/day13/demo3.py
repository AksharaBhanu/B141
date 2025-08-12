import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()
driver.implicitly_wait(10)
driver.get("https://aksharatraining.com/sample16.html")
driver.find_element(By.ID,"ok").click()
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.quit()
