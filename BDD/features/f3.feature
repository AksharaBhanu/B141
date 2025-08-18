Feature: Login
  Scenario Outline: valid login
    Given browser is ready
    When user enters <url>
    Then <title> page is displayed
    Examples:
      |url  | title|
      |google.com| google |
      |fb.com    | fb     |
