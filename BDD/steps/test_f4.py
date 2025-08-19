from pytest_bdd import given,scenario,then,when,parsers

@scenario('f4.feature', 'invalid login')
def test_invalid_login():
    """invalid login."""


@scenario('f4.feature', 'valid login')
def test_valid_login():
    print("""valid login.""")



@given('login page is displayed')
def f2():
    print("""login page is displayed.""")
    

@when(parsers.parse('user enter valid {un} {pw} and click login'))
@when(parsers.parse('user enter invalid {un} {pw} and click login'))
def f3(un,pw):
    print(f"""user enter {un} {pw} and click login.""")
    

@then('home page is displayed')
def f7(ph):
    print("""home page is displayed.""")
    print(ph)

@then('err page is displayed')
def f6():
    print("""err page is displayed.""")
    



    
