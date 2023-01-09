from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session                                                       
 
from InquirerPy.separator import Separator


class StartView(AbstractView):
    """
        La classe StartView hérite la classe mère AbstractView

    """
    def __init__(self):
        
        self.__questions = inquirer.select(
            message=f'Bienvenue à TGVMaximiser!'
            , choices=[
                Separator(' '),
                Choice('Créer votre compte')
                ,
                Separator('--------------'),
                Choice('Se connecter'),
                Separator(' '),
                ],
            
        )

    def display_info(self):

        print(f"Bonjour") 


    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Créer votre compte':
            from view.sign_in_view import SignIn
            return SignIn()

        elif reponse== 'Se connecter':
            from view.connexion_view import ConnexionView
            return ConnexionView()


