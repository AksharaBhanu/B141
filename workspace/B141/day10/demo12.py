import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
file_path=os.path.abspath("MyCV.docx")


driver=Chrome()
driver.get("https://aksharatraining.com/sample7.html")
driver.maximize_window()
time.sleep(2)
#path is not absolute: MyCV.docx
driver.find_element(By.ID,"A2").send_keys(file_path)
time.sleep(3)