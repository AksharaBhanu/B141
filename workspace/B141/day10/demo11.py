import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=Chrome()
driver.get("https://aksharatraining.com/sample7.html")
driver.maximize_window()
time.sleep(2)
#path is not absolute: MyCV.docx
driver.find_element(By.ID,"A2").send_keys("MyCV.docx")
time.sleep(3)