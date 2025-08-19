from pytest_bdd import given,scenario,then,when,parsers

@given('browser is ready',target_fixture='ph')
def f1():
    print("""browser is redy.""")
    ph=123
    return ph

@when('user enters url')
def f5(ph):
    print("""user enters url.""")
    print(ph)
