# Created by cesip at 5/28/2024
Feature: Secondary Page Features


# You can generate a fake email: email-fake.com
  Scenario: User can filter the Secondary deals by "want to sell" option
    Given Open the main page
    When Click sign in from the main page
    And Input email cesipila@gmail.com
    And Input password TestPassword1234
    And Click Continue from sign in page
    And Click on secondary option at the left side menu
    And Click the filters button
    And Click the want to sell listing type
    And click the apply filter button
    Then Verify the secondary page opens
    And Verify all cards have a for sale tag