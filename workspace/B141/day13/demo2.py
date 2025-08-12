import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.CSS_SELECTOR,"p.oxd-userdropdown-name").click()
driver.find_element(By.XPATH,"//a[text()='Logout']").click()
driver.quit()

