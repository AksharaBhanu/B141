import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample10.html")
driver.maximize_window()
time.sleep(1)
#find the element which is above the shadow root, and use .shadow_root==? sr
sr=driver.find_element(By.ID,"shadow_host").shadow_root
#then use sr.find_element instead of driver.find_element
sr.find_element(By.ID,"t1").send_keys("bhanu")
time.sleep(3)