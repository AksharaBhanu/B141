import time
from a_selenium_screenshot_whole_page import get_screenshot_whole_page_with_scroll
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/contact/")
time.sleep(1)
get_screenshot_whole_page_with_scroll(driver, sleepinterval=(0.2, 0.8), save_path='fullpage.png')
time.sleep(1)
driver.quit()