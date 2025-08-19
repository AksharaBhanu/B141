from pytest_bdd import given, when
from selenium.webdriver import Chrome

@given('user opens the chrome browser',target_fixture='driver')
def open_browser():
    print("""user opens the chrome browser.""")
    driver=Chrome()
    driver.implicitly_wait(10)
    return driver


@when('user enters the url')
def ener_url(driver):
    print("""user enters the url.""")
    driver.get("https://pos.aksharatraining.in/pos/public/#")
