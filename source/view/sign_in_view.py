from email.message import Message
from pprint import pprint

from datetime import datetime

from InquirerPy.validator import PasswordValidator
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session
from utilisateur.utilisateur import Utilisateur

from dao.DAOprofil import DAOprofil

ASK_FIRST_NAME=inquirer.text(message = 'What\'s your first name')
ASK_LAST_NAME=inquirer.text(message = 'What\'s your last name?')
ASK_NAISSANCE=inquirer.text(message = 'Quelle est votre date de naissance (sous forme dd/mm/yyyy)?')
ASK_MAIL=inquirer.text(message = 'What\'s your mail')
ASK_PASSWORD=inquirer.secret(message='What\'s your password.'
        ,validate=PasswordValidator(length=8, cap=True, special=True, number=True),
        transformer=lambda _: "[hidden]",
        long_instruction="Password require length of 8, 1 cap char, 1 special char and 1 number char.",)


class SignIn(AbstractView):
    """
        La classe SignIn hérite la classe mère AbstractView.

    """

    def display_info(self):
        print(f"Account creation")
        print(' ')

    def make_choice(self):
        prenom = ASK_FIRST_NAME.execute()
        nom = ASK_LAST_NAME.execute()
        mail = ASK_MAIL.execute()
        used = DAOprofil().verifier_mail(mail)
        while used:
            print('Cette addresse mail a été utilisé. Merci de saisir une autre !')
            mail = ASK_MAIL.execute()
            used = DAOprofil().verifier_mail(mail)

        password =ASK_PASSWORD.execute()
        dateNaissance = ASK_NAISSANCE.execute()
        #dateNaissance = datetime.strptime(dateNaissance, "%d/%m/%Y")
        user = Utilisateur(prenom = prenom
            ,nom = nom
            ,mail = mail
            ,MDP = password
            ,dateNaissance = dateNaissance
        )
        
        created = DAOprofil().creer_compte(user)
        if created:
            Session().user = user
            print('Votre compte a été créé avec succès')
        else:
            print('Vous ne parvenez pas à vous vous inscrire')

        from view.start_view import StartView
        return StartView()
