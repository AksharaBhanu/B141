import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample1.html")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/a").click()
time.sleep(2)