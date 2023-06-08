# Created by khushee at 5/6/23
Feature: Amazon Search tests


 # Scenario: user can search on Amazon
   # Given Open amazon main page
    #When Search for table
    #Then Verify search results shown

 #Scenario:User can search for coffee on Amazon
    #Given open amazon main page
    #When Search for coffee
    #Then Verify search results shown 'coffee'


   Scenario Outline: user can search on Amazon
     Given Open amazon main page
     When Search for <search_word>
     Then Verify search results shown for <search_result>
     Examples:
     |search_word     |search_result  |
     |table           |'table'        |
     |coffee          |'coffee'       |
     |mug             |'mug'          |
     |dress           |'dress'        |