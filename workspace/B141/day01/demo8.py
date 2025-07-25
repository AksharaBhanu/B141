import time
from selenium.webdriver import Chrome

driver=Chrome() #open edge browser
driver.get("http://www.google.com") #enter the url
time.sleep(1)
driver.get("http://www.fb.com")
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(2)
driver.quit()
