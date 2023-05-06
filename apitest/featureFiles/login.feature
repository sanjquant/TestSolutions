Feature: USER Login-Successfull Endpoint Validation

        Background:
	    Given I set sample REST API url


#        Scenario: User Login
#              Given I set a POST user login endpoint
#              When I set HEADER param request content type
#              And set the request body
#              And send POST HTTP request
#              Then I receive valid HTTP response code 200


      Scenario Outline: User Login
              Given I set a POST user login endpoint
              When I set HEADER param request content type
              And set the request body
              And send POST HTTP request
              Then I receive valid HTTP response <StatusCode>
              Examples:
             |StatusCode|
             |200       |
             |200       |
