# Created by khushee at 5/17/23
Feature: Amazon signin test
  # Enter feature description here

  Scenario: verify logged out user sees signin
    Given open amazon search page
    When click on return and orders
    Then verify users see signin
