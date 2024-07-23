# Created by cesip at 7/21/2024
Feature: Connect the company


# You can generate a fake email: email-fake.com
  Scenario: The user can click on “Connect the company” on the left side of the main page
    Given Open the registration page
    When Click sign in from the registration page
    And Input email cesipila@gmail.com and pwd TestPassword1234
    And Click Continue from sign in page
    And Store original window
    And Click on Connect the company
    And Switch to the new support tab
    Then Verify the correct tab opens
