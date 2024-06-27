# Created by cesip at 6/26/2024
Feature: Registration page

  Scenario: The user can enter the info into the input fields on the reg page
    Given Open the registration page
    When Enter some information in the input fields
    Then Verify the right information is present