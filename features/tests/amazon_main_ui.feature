# Created by khushee at 6/6/23
Feature: # Tests for Main Page UI
  # Enter feature description here

  Scenario: # Users see all footer links
    Given Open amazon main page
    Then  verify there are 36 links
    # Enter steps here