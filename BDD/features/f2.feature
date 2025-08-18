Feature: Login
  Scenario: valid login
    Given browser is ready
    When user enters fb.com
    Then fb page is displayed