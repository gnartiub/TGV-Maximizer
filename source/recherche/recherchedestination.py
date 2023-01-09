from recherche.abstractrecherche import AbstractRecherche
from datetime import datetime
import requests as rq

class RechercheDestination(AbstractRecherche):
    """
    La classe RechercheDestination est une classe fille de la classe abstraite AbstractRecherche

    """


    def recherche(self, date, origine, alerter, eligible):
        """
        Aller rechercher des trajets correspondant aux critères 

        Parametres:

            date: str de type dd/mm/yyyy
            origine: str
            alerter: str
            eligible: str

        Retourner:
            L : Liste de URL qui contient le trajet
        """
        

        origine_str = str(origine).replace(" ", "+")
        origine_str = origine_str.upper()

        date_obj = datetime.strptime(date, '%d/%m/%Y')
        jour = str(date_obj.day)
        mois = str(date_obj.month)
        annee = str(date_obj.year)
        
        url ="https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.date=" + annee + "%2F" + mois +  "%2F" + jour + "&exclude.od_happy_card=" + eligible
        
        
        L=[]
        L.append(url)
        dict1= rq.get(url=url)
        dict2=dict1.json()
        datatest=[dict2["records"][k]for k in range(len(dict2["records"]))]
        data=[datatest[k]['fields'] for k in range(len(dict2["records"]))]
        if len(data)==0:
            print("Aucun trajet correspond à votre recherche")
        else:
            for k in range(len(data)):
                print("Le train " + data[k]['train_no'] + " à destination de " + data[k]['destination'] + " partira de " + data[k]['origine'] + " à " +  data[k]['heure_depart'])
        return(L)
        


