from pytest_bdd import scenario, given, when, then, parsers
from apitest.utillib import Utils
import pytest
import requests

utilObj = Utils("register.feature")
FEATURE_NAME = utilObj.get_feature_file_dir()
api_url = None
api_endpoints: dict = {}
request_headers: dict = {}
request_bodies: dict = {}
response_codes: dict = {}
test_data = utilObj.get_test_data("register.json")


@scenario(FEATURE_NAME, "User Registration")
def test_endtest():
    print("End Test")


@given('I set sample REST API url')
def test_geturl():
    global api_url
    api_url = utilObj.base_url
    print("Start the test")


@given('I set a POST user register endpoint')
def test_get_post_endpoint():
    api_endpoints['POST_URL'] = f"{api_url}{utilObj.registerEndPoint}"
    print('url :' + api_endpoints['POST_URL'])


@when('I set HEADER param request content type')
def test_setContentTypeInTheHeader():
    request_headers['Content-Type'] = utilObj.contentType


@when('set the request body')
def test_setRequestBody():
    request_bodies['POST'] = test_data


@when('send POST HTTP request')
def test_sendPostRequestBody():
    response = utilObj.send_post_request(api_endpoints['POST_URL'], request_bodies['POST'], request_headers)
    response_codes['POST'] = response.status_code


@then('I receive valid HTTP response code 200')
def test_validateStatusCode():
    assert response_codes['POST'] == 200
