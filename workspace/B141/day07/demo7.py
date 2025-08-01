import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample1.html")
driver.maximize_window()
time.sleep(2)
print(driver.find_element(By.ID,"a1").tag_name)

print(driver.find_element(By.ID,"a1").get_attribute("href"))
print(driver.find_element(By.ID,"a1").get_attribute("title"))

print(driver.find_element(By.ID,"a1").text)