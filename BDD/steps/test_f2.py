from pytest_bdd import given,scenario,then,when,parsers

@scenario('f2.feature', 'valid login')
def test_valid_login():
    """valid login."""


@given('browser is ready')
def f1():
    print("""browser is ready.""")



@when(parsers.parse('user enters {url}'))
def f2(url):
    print("""user enters """+url)



@then(parsers.parse('{title} page is displayed'))
def f3(title):
    print(f"""{title} page is displayed.""")

