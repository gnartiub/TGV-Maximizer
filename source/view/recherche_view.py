"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session
from recherche.recherchedestination import RechercheDestination
from recherche.recherchetrajet import RechercheTrajet
from recherche.rechercheweekend import RechercheWeekend
from view.choix_view import ChoixView
from dao.DAOtrajet import DAOTrajet


DEPART_SELECTION = inquirer.text(
            message="Votre gare de départ: ")

ARRIVEE_SELECTION = inquirer.text(
            message="Votre gare d'arrivée")

DATE_SELECTION = inquirer.text(
            message="Choisir votre date de départ (sous forme dd/mm/yyyy): ")
ALERTE_SELECTION = inquirer.text(message='Etre alerté?(OUI/NON)')
ELIGIBLE = inquirer.text(
            message="Places eligibles au TGVMax?(OUI/NON)")


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user.nom}, vous cherchez des trajets: '
            , choices=[
                Choice('''Recherche d'un Trajet ''')
                ,Choice('Des destinations atteignables durant un weekend'),
                Choice('Destinations disponibles depuis votre gare')
                ]
        )
        
    def display_info(self):
        print(f"Hello {Session().user.nom}, veuillez saisir vos critères")

    def make_choice(self):
        response = self.__questions.execute()

        if response == '''Recherche d'un Trajet ''':
            depart = DEPART_SELECTION.execute()
            arrivee = ARRIVEE_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            url = RechercheTrajet().recherche(date=date,origine=depart,destination=arrivee,alerter=alerter,eligible=eligible)
            
            DAOTrajet().DAOTrajet(url=url,typerech="trajet",date=date,origine=depart,destination=arrivee,alerter=alerter,eligible=eligible)
            
            
            
            return ChoixView()

        elif response== 'Des destinations atteignables durant un weekend':
            depart = DEPART_SELECTION.execute()
            arrivee = ARRIVEE_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            url = RechercheWeekend().recherche(date=date,origine=depart,destination=arrivee, alerter=alerter, eligible=eligible)
            DAOTrajet().DAOTrajet(url=url,typerech="weekend",date=date,origine=depart,destination=arrivee, alerter=alerter, eligible=eligible)
            
            
            return ChoixView()
        
        elif response=='Destinations disponibles depuis votre gare':
            depart = DEPART_SELECTION.execute()
            date = DATE_SELECTION.execute()
            alerter = ALERTE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            url = RechercheDestination().recherche(date=date,origine=depart,alerter=alerter,eligible=eligible)
            DAOTrajet().DAOTrajet(url=url,typerech="destination",date=date,origine=depart,alerter=alerter,eligible=eligible,destination="none")
            return ChoixView()


