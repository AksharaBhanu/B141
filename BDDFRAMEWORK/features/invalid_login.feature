Feature: login functionality of POS application
  Background:
    Given user opens the chrome browser
    When user enters the url

  Scenario: Invalid Login
    Given login page is displayed
    When user enter abc username
    And user enter xyz password
    And user clicks on go button
    Then ErrMsg is displayed