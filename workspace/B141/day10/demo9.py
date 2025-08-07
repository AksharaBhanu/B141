import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(1)
xp1="//input[@placeholder='Enter Mobile Number']"
driver.find_element(By.XPATH,xp1).send_keys("9481787493")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"span.commonModal__close").click()
time.sleep(2)