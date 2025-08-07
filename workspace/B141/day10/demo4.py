import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample14.html")
listbox=driver.find_element(By.ID,"A2")
select=Select(listbox) #create Select class object

all_options=select.options #get all options present in list box
count=len(all_options) #count it
print(count) #4
#select all
for i in range(count):
    select.select_by_index(i)
#select in reverse order
#select alternative options

time.sleep(2)

