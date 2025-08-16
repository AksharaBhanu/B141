import time
from selenium.webdriver import Firefox

driver=Firefox() #open edge browser
driver.get("http://www.google.com") #enter the url
time.sleep(8)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.close()
time.sleep(2)

