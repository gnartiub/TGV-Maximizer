from abc import ABC, abstractmethod

class AbstractRecherche(ABC):
    """
    An abstract Recherche. As an abstract class, it as to be inherited
    """
    @abstractmethod
    def recherche(self):
        
        """
        Une méthode abstraite qui va aller chercher des trajets par API SNCF

        Returns :
            List(url) :  une liste des url. Chaque url contient 1 trajet
        """
        pass