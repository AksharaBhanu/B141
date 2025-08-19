from pytest_bdd import scenario
from steps.page_f5 import *  #* means all the functions

@scenario('f5.feature', 'open login page')
def test_open_login_page():
    print("""open login page.""")

