import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample13.html")
time.sleep(1)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
time.sleep(1)
select.select_by_index(1) #select 2nd option
time.sleep(1)
select.select_by_value("c") #select option by value c
time.sleep(1)
select.select_by_visible_text("Delhi")
time.sleep(1)