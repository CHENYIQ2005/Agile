Feature: Gestion complète d'une série avec acteur et saisons

  En tant que gestionnaire de séries,
  Je veux pouvoir associer un acteur principal à une série,
  Et ajouter des saisons à la série,
  Afin de gérer à la fois les informations artistiques et de production.

  Scenario Outline: Associer un acteur et ajouter une saison à une série
    Given une série intitulée "<titre>" avec <saisons> saison(s)
    And un acteur nommé "<acteur>"
    When j’associe l’acteur à la série
    And j’ajoute une nouvelle saison
    Then le nom de l’acteur principal de la série est "<acteur>"
    And la série doit avoir <attendu> saison(s)

    Examples:
      | titre            | acteur         | saisons | attendu |
      | The four seasons | Tina Fey       | 1       | 2       |
      | Dark             | Anna Müller    | 2       | 3       |
      | Dix Pour Cent    | Camille Cottin | 3       | 4       |
