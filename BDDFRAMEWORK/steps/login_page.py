from pytest_bdd import given,when,parsers,then

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given('login page is displayed')
def login_page(driver):
    print("""login page is displayed.""")
    title=driver.title
    print('title is:',title)
    assert 'Login' in title


@when(parsers.parse('user enter {type} username'))
def enter_username(driver:Chrome,type):
    print("""user enter valid username.""")
    driver.find_element(By.ID,"input-username").send_keys(type)

@when(parsers.parse('user enter {type} password'))
def enter_password(driver:Chrome):
    print("""user enter valid password.""")
    driver.find_element(By.NAME,"password").send_keys("pointofsale")

@when('user clicks on go button')
def click_go_button(driver:Chrome):
    print("""user clicks on go button.""")
    driver.find_element(By.NAME,"login-button").click()

@then('ErrMsg is displayed')
def verify_errormsg(driver:Chrome):
    print("ErrMsg is displayed")
    assert driver.find_element(By.CSS_SELECTOR,"div.error").is_displayed()
    print('ERR MSG IS:',driver.find_element(By.CSS_SELECTOR,"div.error").text)








