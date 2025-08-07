import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample14.html")
time.sleep(1)
mslb=driver.find_element(By.ID,"A3")
select=Select(mslb) #create Select class obnject
time.sleep(1)
select.deselect_all()
time.sleep(1)