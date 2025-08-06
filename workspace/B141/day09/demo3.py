import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample3.html")
time.sleep(1)
all_textbox=driver.find_elements(By.XPATH,"//input[@type='text']")
print(len(all_textbox))

# element=all_textbox[0]
# element.clear()

for element in all_textbox:
    element.clear()


time.sleep(3)
data=['Jaspreet','bhanu','akshara','yash']
i=0
for elemet in all_textbox:
    elemet.send_keys(data[i])
    i=i+1

time.sleep(3)