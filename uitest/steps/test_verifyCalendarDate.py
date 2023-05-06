from pytest_bdd import scenario, given, when, then, parsers
# from selenium.webdriver.chrome import webdriver
#
# from apitest.utillib import Utils
# import pytest
# import requests
from uitest.seleniumUtil import Util
from uitest.pageObjects.marketData import MarketData
from uitest.pageObjects.pageLogin import Login

utl = Util("marketDataCalendar.feature")
FEATURE_NAME = utl.get_feature_file_dir()
driver = utl.get_driver_chome_service()
mkdata = MarketData(driver)
login = Login(driver)
username = utl.read_excel_data()["username"][0]
password = utl.read_excel_data()["password"][0]


@scenario(FEATURE_NAME, "Verify MarketData Calendar date")
def test_run_cleanups():
    print("End the test")
    login.close_browser()


@given('User open the Browser and navigated to login page of yahoo')
def navigate_to_login_page():
    print("Start the test")
    login.launch_browser()


@when('User enters username')
def enter_username():
    print("User enters ")
    login.set_username(username)


@when('Click the user next button')
def click_on_user_next():
    print("Click the user next button")
    login.click_on_next_button()


@when('enter password')
def enter_password():
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


@then(parsers.cfparse('verify that the "{financelinkName}" link exists and click on the finance link'))
def navigate_to_yahoo_home_page(financelinkName):
    print(financelinkName)
    finance_link_name = mkdata.get_finance_link_name()
    assert finance_link_name == financelinkName
    mkdata.click_on_finance_link()


@then('Click on MarketData link')
def click_on_market_data_link():
    print("Click on MarketData link")
    mkdata.click_on_market_data_link()


@then('Click on MarketData link')
def click_on_market_data_link():
    print("Click on MarketData link")
    mkdata.click_on_market_data_link()


@then('Under market data link navigate to calendar')
def click_on_calendar_link():
    print("Under market data link navigate to calendar")
    mkdata.click_on_calendar_link()


@then('verify that todays date is displayed')
def verify_todays_date_is_displayed():
    print(f"verify that today's date is displayed as :  {utl.get_todays_date()}")
    calendar_dates = mkdata.get_all_dates()
    print(calendar_dates)
    assert True, mkdata.match_date(utl.get_todays_date())
