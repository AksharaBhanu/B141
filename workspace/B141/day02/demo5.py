import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample2.html") #enter the url
driver.find_element(By.TAG_NAME,"a").click()
time.sleep(1)
driver.quit()