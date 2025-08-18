from pytest_bdd import given,scenario,then,when


@scenario('./../features/f1.feature', 'valid login')
def test_valid_login():
    print("""valid login.""")


@given('login page is displayed')
def f1():
     print("""login page is displayed.""")



@when('user enter valid un pw and click login')
def f2():
     print("""user enter valid un pw and click login.""")



@then('home page is displayed')
def f3():
     print("""home page is displayed.""")

