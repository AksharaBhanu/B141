import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome() #open the chrome browser
time.sleep(1)
driver.get("https://aksharatraining.com/sample1.html") #enter the url
time.sleep(1)
element=driver.find_element(By.TAG_NAME,"a") #find element by tag 'a'
time.sleep(1)
element.click() #click on that element
time.sleep(1)
driver.quit()