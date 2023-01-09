from email.message import Message
from pprint import pprint


from InquirerPy.validator import PasswordValidator
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session
from utilisateur.utilisateur import Utilisateur

from dao.DAOprofil import DAOprofil

ASK_USERNAME=inquirer.text(message = 'Quel est votre mail ?')
ASK_PASSWORD=inquirer.secret(message='Quel est votre MDP ?',
        transformer=lambda _: "[hidden]",)


class ConnexionView(AbstractView):


    def display_info(self):
        print(f"CONNEXION")
        print(' ')

    def make_choice(self):
        mail = ASK_USERNAME.execute()
        MDP =ASK_PASSWORD.execute()
        
        ####### VERIFICATION  DE L'EXISTANCE DU COMPTE #####

        if DAOprofil().connexion(mail,MDP)!=0:
            print("Felicitations, vous êtes connectez")
            Session().user = DAOprofil().connexion(mail,MDP)
            from view.choix_view import ChoixView
            return ChoixView()

        else:
            print('Username ou mot de passe incorrect')
            from view.start_view import StartView
            return StartView()
