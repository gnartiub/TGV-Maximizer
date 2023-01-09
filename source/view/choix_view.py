from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import sys
from view.abstract_view import AbstractView
from view.session import Session
from InquirerPy.separator import Separator

class ChoixView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Que souhaitez vous faire ?'
            , choices=[
                Separator(' ')
                ,Choice('Se déconnecter')
                ,Separator('------------------')
                ,Choice('Faire une recherche')
                ,Separator('------------------')
                ,Choice('Gérer votre compte')
                ,Separator(' ')]
        )
        
    def display_info(self):
        print(f"Bonjour") 

    def make_choice(self):
        response = self.__questions.execute()

        if response == 'Faire une recherche':
            from view.recherche_view import RechercheView
            return RechercheView()

        elif response== 'Se déconnecter':
            Session().user = None
            Session().list_trajet = None
            sys.exit()

        elif response == 'Gérer votre compte':
            from view.change_info_view import ChangerInfo
            return ChangerInfo()


