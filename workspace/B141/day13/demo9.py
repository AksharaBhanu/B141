import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#NoSuchElementException
#solution1--implicitly wait
#solution2--time sleep
#solution3-WebDriverWait (explicit wait) -- we specify waiting condition explicitly
#solution4-custom wait
driver=Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
for i in range(100):
    try:
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        print('Element found')
        break
    except:
        print('No Element',i)

print('Done')