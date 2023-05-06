Feature: Get List of of all the resources

    Background:
	    Given I set sample REST API url

    Scenario: Verify Response Resources
        Given I set a GET resources endpoint
        When I set HEADER param request content type
        And send GET HTTP request
        Then I receive valid HTTP response code 200
        And verify one of the ids and resources
        And verify all Ids
        And verify all names
        And verify all years
        And verify all colors
        And verify all pantone_values
