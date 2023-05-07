# Created by khushee at 5/6/23
Feature: Amazon Search tests
  # Enter feature description here

  Scenario: user can search on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown
