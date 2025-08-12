import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample10.html")
driver.maximize_window()
time.sleep(1)

sr=driver.find_element(By.XPATH,"/html/body/div[2]").shadow_root
sr.find_element(By.CSS_SELECTOR,"#c1").click()
sr.find_element(By.ID,"t1").send_keys("bhanu")
time.sleep(3)