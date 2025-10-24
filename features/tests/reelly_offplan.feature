Feature: Verify Off-plan filtering on Reelly

  Scenario: User can filter Off-plan projects by Announced status
    Given Open Reelly main page
    And Log in to Reelly account
    When Click on "Off-plan" in left side menu
    Then Verify Off-plan page is opened
    When Filter by sale status "Announced"
    Then Verify all projects have status "Announced"
