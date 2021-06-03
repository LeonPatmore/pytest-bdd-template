Feature: Some Feature

  Scenario: Simple example
    Given I'm an user
    When I do something
    Then I get something

  Scenario: Test using global given
    Given I'm a global user
    When I do something
    Then I get something

  Scenario: Failing test
    Given I'm a global user
    When I do something
    Then This fails
