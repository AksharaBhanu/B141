import time

from selenium.webdriver import Chrome


driver=Chrome()
start=time.time()#6:34:20
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
end=time.time()#6:34:23
print(end-start)