import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

expected=['Agra','Bangalore','Chennai','Delhi']

driver=Chrome()
driver.get("https://aksharatraining.com/sample13.html")
time.sleep(1)
listbox=driver.find_element(By.ID,"A1")
select=Select(listbox)
all_options=select.options

actual=[] #create empty list

for option in all_options:
    actual.append(option.text)

print(expected)
print(actual)

if actual==expected:
    print('Pass')
else:
    print('Fail')