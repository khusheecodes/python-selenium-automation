# Created by khushee at 6/6/23
Feature:  Amazon Bestsellers
  # verifying there are 5 links

  Scenario: # Users verify 5 links in bestsellers
    Given Open amazon main page
    When click on best sellers
    Then Verify there are 5 links