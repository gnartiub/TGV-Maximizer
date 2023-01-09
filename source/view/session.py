from typing import List
from utils.singleton import Singleton

from utilisateur.utilisateur import Utilisateur

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.user: Utilisateur = None

