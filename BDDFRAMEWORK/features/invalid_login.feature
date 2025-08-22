Feature: login functionality of POS application
  Background:
    Given user opens the chrome browser
    When user enters the url

  Scenario Outline: Invalid Login
    Given login page is displayed
    When user enter <un> username
    And user enter <pw> password
    And user clicks on go button
    Then ErrMsg is displayed
    Examples:
      |un  |pw|
      |ab  |xy|
      |admin|123|
      |amin |pointofsale|
      |a  |c            |