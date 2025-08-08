import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=Chrome()
driver.get("https://aksharatraining.com/parent.html")
time.sleep(1)
driver.find_element(By.ID,"a1").click()
time.sleep(1)
all=driver.window_handles #adress of all browsers
print(len(all))
for w in all:
    driver.switch_to.window(w)
    print(driver.current_window_handle)
    print(w,driver.title)
    driver.close()
    time.sleep(1)
