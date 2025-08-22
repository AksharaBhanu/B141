import pytest
from pytest_bdd import scenario
from steps.login_page import *
from steps.home_page import *

@pytest.mark.order(1)
@scenario('valid_login.feature', 'Valid Login')
def test_valid_login():
    print("""Valid Login scenario completed""")
