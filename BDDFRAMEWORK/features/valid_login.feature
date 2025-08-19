Feature: login functionality of POS application
  Background:
    Given user opens the chrome browser
    When user enters the url

  Scenario: Valid Login
    Given login page is displayed
    When user enter valid username
    And user enter valid password
    And user clicks on go button
    Then Home Page is displayed