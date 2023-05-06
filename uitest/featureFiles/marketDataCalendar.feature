Feature: Read login credentials from excel and validate the current calendar date



Scenario: Verify MarketData Calendar date
    Given User open the Browser and navigated to login page of yahoo
    When User enters username
    And Click the user next button
    And enter password
    And Click the password next button
    Then User navigates to Yahoo home page
    And verify that the "Finance" link exists and click on the finance link
    And Click on MarketData link
    And Under market data link navigate to calendar
    Then verify that todays date is displayed

