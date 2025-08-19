from pytest_bdd import then
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

@then('Home Page is displayed')
def verify_home_page(driver:Chrome):
    print("""Home Page is displayed.""")
    assert driver.find_element(By.XPATH,"//a[text()='Logout']").is_displayed()

