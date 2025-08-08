import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--disable-notifications")
driver=Chrome(options)
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='OK']").click()
time.sleep(2)
driver.find_element(By.ID,'disha-banner-close').click()
time.sleep(6)
