# Created by cesip at 5/31/2024
Feature: Whatsapp and Telegram communities

  @smoke @regression
  Scenario: 12 User access to Whatsapp and Telegram communities
    Given Open the main page
    When Click sign in from the main page
    And Input email cesipila@gmail.com and pwd TestPassword1234
    And Click Continue from sign in page
    And Click on settings at the left side menu
    And Store original window
    And Click on support option
    And Switch to the new support tab
    Then Verify the support page opens
    And Go back to settings page
    And Click on news option
    Then Verify the news page opens