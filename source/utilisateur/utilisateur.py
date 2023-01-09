
from datetime import datetime


class Utilisateur():
    """
        La classe Utilisateur permet de créer un objet d'utilisateur 

    """
    def __init__(self,
        id  = None,
        mail = None,
        prenom= None,
        nom= None,
        MDP= None,
        dateNaissance= None):

        self._id :int =id
        self._mail:str=mail
        self._MDP:str=MDP
        self._dateNaissance:str=dateNaissance
        self._nom:str = nom
        self._prenom:str = prenom


    @property
    def id(self):
        """The id property."""
        return self._id
    
    @property
    def nom(self):
        """The nom property."""
        return self._nom
    
    @property
    def prenom(self):
        """The prenom property."""
        return self._prenom
    @property
    def mail(self):
        """The mail property."""
        return self._mail

    @property
    def MDP(self):
        """The mail property."""
        return self._MDP

    @property
    def dateNaissance(self):
        """The date_naissance property."""
        return self._dateNaissance


    @mail.setter
    def mail(self, value):
        self._mail = value

    @MDP.setter
    def MDP(self, value):
        self._MDP = value

    @dateNaissance.setter
    def dateNaissance(self, value):
        self.dateNaissance = value