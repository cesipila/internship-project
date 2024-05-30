# Created by cesip at 5/28/2024
Feature: Off-Plan Page Features


# You can generate a fake email: email-fake.com
  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page
    When Click sign in from the main page
    And Input email cesipila@gmail.com and pwd TestPassword1234
    And Click Continue from sign in page
    And Click on off plan at the left side menu
    And Verify the right page opens
    And Click the off-plan filters button
    And Set the range from 1200000 to 2000000
    And Click the off-plan apply filter button
    Then Verify the price in all cards is within 1200000 to 20000000 range
