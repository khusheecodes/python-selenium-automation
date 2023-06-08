# Created by khushee at 5/17/23
Feature: Amazon empty cart test
  # Enter feature description here

  Scenario: # Enter scenario name here
    Given open amazon page
    When click on cart
    Then verify cart is empty

  Scenario: User can add a product to the cart
    Given Open amazon main page
    When Search for Table
    And Click on the first product
    And Store product name
    And Click on Add to cart Button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
      