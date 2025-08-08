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
driver.switch_to.window("Akshara")
time.sleep(1)
driver.find_element(By.ID,"t1").send_keys("Hi")
time.sleep(1)
driver.switch_to.window("Swara")
driver.find_element(By.ID,"t2").send_keys("Bye")
time.sleep(2)
driver.quit()

