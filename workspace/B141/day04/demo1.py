import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
driver.get("https://aksharatraining.com/sample1.html")
# print("this is 'python' code")
# print('this is "python" code')
# driver.find_element(By.CSS_SELECTOR,"a[name='n1']").click()
driver.find_element(By.CSS_SELECTOR,'a[name="n1"]').click()
time.sleep(3)