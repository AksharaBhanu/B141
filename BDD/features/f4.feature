Feature: Login
  Background:
    Given browser is ready
    When  user enters url

  Scenario: valid login
    Given login page is displayed
    When user enter valid admin admin123 and click login
    Then home page is displayed

  Scenario: invalid login
      Given login page is displayed
      When user enter invalid bhanu bhanu123 and click login
      Then err page is displayed
