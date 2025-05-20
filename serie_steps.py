from dataclasses import dataclass
from behave import given, when, then
from src.serie import Serie

@dataclass
class SerieSteps:
    serie: Serie = None

# Scenario

@given('une série intitulée "Astérix" avec 4 saisons')
def given_asterix_with_4_seasons(context):
    context.steps = SerieSteps(serie=Serie(titre="Astérix", nb_saisons=4))

@when("j’ajoute une nouvelle saison")
def when_add_one_season(context):
    context.steps.serie.ajouter_saison()

@then("la série doit avoir 5 saisons")
def then_should_have_5_seasons(context):
    assert context.steps.serie.nb_saisons == 5


# Scenario Outline

@given('une série intitulée "{titre}" avec {saisons:d} saisons')
def given_serie_with_params(context, titre, saisons):
    context.steps = SerieSteps(serie=Serie(titre=titre, nb_saisons=saisons))

@then("la série doit avoir {attendu:d} saisons")
def then_serie_should_have_expected_seasons(context, attendu):
    assert context.steps.serie.nb_saisons == attendu
