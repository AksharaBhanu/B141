import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample14.html")
listbox=driver.find_element(By.ID,"A3")
select=Select(listbox) #create Select class object

all_options=select.all_selected_options
for option in all_options:
    print(option.text)
