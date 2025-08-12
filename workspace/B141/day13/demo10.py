from selenium.webdriver import Chrome


driver=Chrome()
driver.set_page_load_timeout(3)
try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print('page is loaded with in 3s')
except:
    print('page is NOT loaded with in 3s')
