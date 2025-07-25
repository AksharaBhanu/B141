import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample1.html") #enter the url
driver.find_element(By.TAG_NAME,"t").click()
driver.quit()