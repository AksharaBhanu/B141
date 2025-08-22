import pytest
from pytest_bdd import scenario
from steps.login_page import *
from steps.home_page import *

@pytest.mark.order(2)
@scenario('invalid_login.feature', 'Invalid Login')
def test_invalid_login():
    print("""Invalid Login scenario completed""")
