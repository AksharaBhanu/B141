import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://shop.polymer-project.org/")
driver.maximize_window()
time.sleep(1)

outer_sr=driver.find_element(By.XPATH,"/html/body/shop-app").shadow_root
inner_sr=outer_sr.find_element(By.NAME,"home").shadow_root
xp="//a[text()='Shop Now']"
all_link=inner_sr.find_elements(By.CSS_SELECTOR,"a")
print(len(all_link))

for link in all_link:
    print(link.get_attribute("aria-label"))


all_link[0].click()

time.sleep(4)

