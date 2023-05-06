Feature: Login to the application with different credentials




Scenario Outline: Test multiple login functionality
    Given User open the Browser and navigated to login page of yahoo
    When User enters "<username>"
    And Click the user next button
    And enter "<password>"
    And Click the password next button
    Then User navigates to Yahoo home page
    And verify that the "Finance" link exists
  Examples:
    | username        | password  |
    |FirstTestLogin_12|TestAbc_12!|
    |SecondTestLogin  |TestAbc_12!|
    |ThirdTestLogin   |TestAbc_12!|