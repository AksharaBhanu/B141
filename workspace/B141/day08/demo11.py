#double click --context click--context menu
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



driver=Chrome()
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
driver.maximize_window()
time.sleep(1)
before=driver.find_element(By.ID,"box").text
print(before)

button=driver.find_element(By.XPATH,"//input[@type='button']")
action_chains=ActionChains(driver)
action_chains.double_click(button).perform()
time.sleep(2)

after=driver.find_element(By.ID,"box").text
print(after)


