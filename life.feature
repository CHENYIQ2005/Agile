Feature: Person Relationships and Life Events

  As a simcity designer
  I want to simulate people and interactions
  So that I can play and learn


  Scenario: Popeye celebrates a birthday
    Given a person named Popeye who is 16 years old
    When Popeye celebrates a birthday
    Then Popeye should be 17 years old


  Scenario Outline: Person celebrates a birthday
    Given Person named <name> who is <age> years old
    When they celebrate a birthday
    Then they should be <older>

    Examples:
      | name   | age | older |
      | Popeye | 16  | 17    |
      | Olive  | 18  | 19    |
      | Brutus | 20  | 21    |
      | Ahmed  | 25  | 26    |
      | Fabien | 23  | 24    |
