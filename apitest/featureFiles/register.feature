Feature: USER Registration-Successfull Endpoint Validation

    Background:
	    Given I set sample REST API url

    Scenario: User Registration
        Given I set a POST user register endpoint
        When I set HEADER param request content type
        And set the request body
        And send POST HTTP request
        Then I receive valid HTTP response code 200

