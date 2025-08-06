import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample3.html")

all_textbox=driver.find_elements(By.XPATH,"//input[@type='text']")

for element in all_textbox:
    element.clear()


data=['Jaspreet','bhanu','akshara','yash']

for e,input in zip(all_textbox,data):
    e.send_keys(input)


time.sleep(3)