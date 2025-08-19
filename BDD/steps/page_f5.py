from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium.webdriver import Firefox


@given('user opens chrome browser',target_fixture='driver')
def f1():
    print('user opens chrome browser')
    driver=Firefox()
    return driver


@when('user enter the url')
def f2(driver):
    print("""user enter the url.""")
    driver.get("http://www.google.com")
    


@then('Login page is displayed')
def f3(driver):
    print("""Login page is displayed.""")
    print(driver.title)
