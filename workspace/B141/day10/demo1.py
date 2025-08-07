import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/sample14.html")
time.sleep(1)
sslb=driver.find_element(By.ID,"A1")
select1=Select(sslb)
print(select1.is_multiple) #is it multi select list box-->No--> False None

mslb=driver.find_element(By.ID,"A2")
select2=Select(mslb)
print(select2.is_multiple) #is it multi select list box-->Yes--> True