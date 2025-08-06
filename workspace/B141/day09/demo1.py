import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample2.html")
time.sleep(1)
all_elements=driver.find_elements(By.TAG_NAME,"a")
print(len(all_elements)) #list[e1,e2,e3]

first_element=all_elements[0]
print(first_element.text)
print(first_element.get_attribute("href"))

print(all_elements[1].get_attribute("href"))
print(all_elements[2].get_attribute("href"))