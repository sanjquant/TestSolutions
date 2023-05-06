from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.chrome import webdriver

from uitest.seleniumUtil import Util
from uitest.pageObjects.marketData import MarketData
from uitest.pageObjects.pageLogin import Login


utl = Util("login.feature")
FEATURE_NAME = utl.get_feature_file_dir()
driver: webdriver
mkdata: MarketData
login: Login


@scenario(FEATURE_NAME, "Test multiple login functionality")
def test_run_cleanups():
    print("End the test")
    login.close_browser()


@given('User open the Browser and navigated to login page of yahoo')
def navigate_to_login_page():
    print("Start the test")
    global driver, mkdata, login
    driver = utl.get_driver_chome_service()
    mkdata = MarketData(driver)
    login = Login(driver)
    login.launch_browser()


@when(parsers.cfparse('User enters "{username}"'))
def enter_username(username):
    print("User enters ")
    login.set_username(username)


@when('Click the user next button')
def click_on_user_next():
    print("Click the user next button")
    login.click_on_next_button()


@when(parsers.cfparse('enter "{password}"'))
def enter_password(password):
    print("enter password")
    login.set_password(password)


@when('Click the password next button')
def click_on_password_next():
    print("Click the password next button")
    login.click_on_next_password_button()


@then('User navigates to Yahoo home page')
def navigate_to_yahoo_home_page():
    print("User navigates to Yahoo home page")
    actual_home_page_name = mkdata.get_home_page_name()
    assert actual_home_page_name == "Yahoo Home"


@then(parsers.cfparse('verify that the "{financelinkName}" link exists'))
def navigate_to_yahoo_home_page(financelinkName):
    print(financelinkName)
    finance_link_name = mkdata.get_finance_link_name()
    assert finance_link_name == financelinkName
