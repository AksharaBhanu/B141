from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given('login page is displayed')
def login_page(driver):
    print("""login page is displayed.""")
    title=driver.title
    print('title is:',title)
    assert 'Login' in title


    

@when('user enter valid username')
def enter_username(driver:Chrome):
    print("""user enter valid username.""")
    driver.find_element(By.ID,"input-username").send_keys("admin")

@when('user enter valid password')
def enter_password(driver:Chrome):
    print("""user enter valid password.""")
    driver.find_element(By.NAME,"password").send_keys("pointofsale")

@when('user clicks on go button')
def click_go_button(driver:Chrome):
    print("""user clicks on go button.""")
    driver.find_element(By.NAME,"login-button").click()








