from pytest_bdd import scenario, given, when, then, scenarios
from apitest.utillib import Utils

utilObj = Utils("resources.feature")
FEATURE_NAME = utilObj.get_feature_file_dir()
api_url = None
api_endpoints: dict = {}
request_headers: dict = {}
response_data: dict = {}
response_codes: dict = {}
expected_testdata = utilObj.get_test_data("resources.json")


@scenario(FEATURE_NAME, "Verify Response Resources")
@given('I set sample REST API url')
def test_geturl():
    print("Start the test")
    global api_url
    api_url = utilObj.base_url


@given('I set a GET resources endpoint')
def test_get_post_endpoint():
    api_endpoints['GET_URL'] = f"{api_url}{utilObj.registerEndPoint}"
    print('url :' + api_endpoints['GET_URL'])


@when('I set HEADER param request content type')
def test_setContentTypeInTheHeader():
    request_headers['Content-Type'] = utilObj.contentType


@when('send GET HTTP request')
def test_sendGetRequest():
    response = utilObj.send_get_request(api_endpoints['GET_URL'], request_headers)
    response_codes['GET'] = response.status_code
    response_data['Content'] = response.text


@then('I receive valid HTTP response code 200')
def test_validateStatusCode():
    assert response_codes['GET'] == 200


@then('verify one of the ids and resources')
def test_verifyIdAndResources():
    actual_data = utilObj.get_json_value("$.data", response_data['Content'])
    assert expected_testdata['data'][0]['id'] == actual_data[0].value[0]['id']
    assert expected_testdata['data'][0]['name'] == actual_data[0].value[0]['name']
    assert expected_testdata['data'][0]['year'] == actual_data[0].value[0]['year']
    assert expected_testdata['data'][0]['color'] == actual_data[0].value[0]['color']
    assert expected_testdata['data'][0]['pantone_value'] == actual_data[0].value[0]['pantone_value']


@then('verify all Ids')
def test_verify_all_ids():
    actual_ids = [each.value for each in utilObj.get_json_value("$.data[*].id", response_data['Content'])]
    expected_data = [each['id'] for each in expected_testdata['data']]
    assert len(actual_ids) == len(expected_data)
    assert sorted(actual_ids) == sorted(expected_data)


@then('verify all names')
def test_verify_all_names():
    actual_names = [each.value for each in utilObj.get_json_value("$.data[*].name", response_data['Content'])]
    expected_names = [each['name'] for each in expected_testdata['data']]
    assert len(actual_names) == len(expected_names)
    assert sorted(actual_names) == sorted(expected_names)


@then('verify all years')
def test_verify_all_years():
    actual_names = [each.value for each in utilObj.get_json_value("$.data[*].year", response_data['Content'])]
    expected_names = [each['year'] for each in expected_testdata['data']]
    assert len(actual_names) == len(expected_names)
    assert sorted(actual_names) == sorted(expected_names)


@then('verify all colors')
def test_verify_all_colors():
    actual_colors = [each.value for each in utilObj.get_json_value("$.data[*].color", response_data['Content'])]
    expected_colors = [each['color'] for each in expected_testdata['data']]
    assert len(actual_colors) == len(expected_colors)
    assert sorted(actual_colors) == sorted(expected_colors)


@then('verify all pantone_values')
def test_verify_all_pantone_values():
    actual_pantone_values = [each.value for each in
                             utilObj.get_json_value("$.data[*].pantone_value", response_data['Content'])]
    expected_pantone_values = [each['pantone_value'] for each in expected_testdata['data']]
    assert len(actual_pantone_values) == len(expected_pantone_values)
    assert sorted(actual_pantone_values) == sorted(expected_pantone_values)
