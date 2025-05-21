from behave import given, when, then
from Serie import Serie
from Acteur import Acteur


class SerieLogic:


    @given('une série intitulée "{titre}" avec {nb:d} saison(s)')
    def step_create_serie(context, titre, nb):
        context.logic = SerieLogic()
        context.logic.creer_serie(titre, nb)

    @given('un acteur nommé "{nom}"')
    def step_create_acteur(context, nom):
        context.logic.associer_acteur(nom)

    @when("j’associe l’acteur à la série")
    def step_associate(context):
        pass  # déjà fait dans le step précédent

    @when("j’ajoute une nouvelle saison")
    def step_add_season(context):
        context.logic.ajouter_saison()

    @then('le nom de l’acteur principal de la série est "{attendu}"')
    def step_check_acteur_nom(context, attendu):
        assert context.logic.get_acteur_nom() == attendu, f"Attendu: {attendu}, Obtenu: {context.logic.get_acteur_nom()}"

    @then("la série doit avoir {attendu:d} saison(s)")
    def step_check_nb_saisons(context, attendu):
        assert context.logic.get_nb_saisons() == attendu, f"Attendu: {attendu}, Obtenu: {context.logic.get_nb_saisons()}"
