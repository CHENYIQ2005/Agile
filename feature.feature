Feature: Association d'un acteur à une série

  En tant que gestionnaire de séries,
  Je veux pouvoir associer un acteur principal à une série,
  Afin de retrouver facilement l'acteur principal d'une série.

  Scenario Outline: Associer un acteur à une série et vérifier le nom de l'acteur
    Given une série intitulée "<titre>"
    And un acteur nommé "<acteur>"
    When j’associe l’acteur à la série
    Then le nom de l’acteur principal de la série est "<acteur>"

    Examples:
      | titre             | acteur         |
      | Les Revenants     | Pierre Dupont  |
      | Dark              | Anna Müller    |

  Scenario Outline: Remplacer l’acteur associé à une série
    Given une série intitulée "<titre>"
    And un acteur nommé "<ancien>"
    And un acteur nommé "<nouveau>"
    When j’associe "<ancien>" à la série
    And j’associe "<nouveau>" à la série
    Then le nom de l’acteur principal de la série est "<nouveau>"

    Examples:
      | titre           | ancien         | nouveau         |
      | Lupin           | Omar Sy        | Jean Reno       |
