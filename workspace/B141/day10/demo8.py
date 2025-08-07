#right click --context click--context menu
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver=Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(1)

xp="//span[text()='right click me']"
button=driver.find_element(By.XPATH,xp)
actions_actions=ActionChains(driver)
actions_actions.context_click(button).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Copy']").click()
time.sleep(2)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)