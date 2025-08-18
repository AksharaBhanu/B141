Feature: Login
  Scenario: valid login
    Given login page is displayed
    When user enter valid un pw and click login
    Then home page is displayed