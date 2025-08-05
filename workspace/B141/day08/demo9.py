#mouse hover--> drop down menu
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=Chrome()
driver.get("https://www.globalsqa.com/")
driver.maximize_window()
time.sleep(1)
menu=driver.find_element(By.XPATH,"(//a[text()='Free Ebooks'])[1]")
action_chains=ActionChains(driver)
action_chains.move_to_element(menu).perform()
time.sleep(2)

xp="//span[text()='Free Machine Learning Ebooks']"
driver.find_element(By.XPATH,xp).click()
time.sleep(2)