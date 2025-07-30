import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample15.html")
time.sleep(2)
xp="//td[text()='API']/../td[1]/input"
driver.find_element(By.XPATH,xp).click()
time.sleep(3)
