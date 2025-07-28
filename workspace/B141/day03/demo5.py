import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample1.html")
driver.find_element(By.LINK_TEXT,"Google").click()
time.sleep(2)
driver.quit()