from recherche.abstractrecherche import AbstractRecherche

from datetime import datetime
import requests as rq

class RechercheTrajet(AbstractRecherche):
    
    def recherche(self,date, origine, destination, alerter = False, eligible = "OUI"):
        """
        Aller rechercher des trajets correspondant aux critères 

        Parametres:

            date: str de type dd/mm/yyyy
            origine: str
            destination: str
            alerter: bool
            eligible: str

        Retourner:
            L : Liste de URL qui contient le trajet
        """
        
        origine_str = str(origine).replace(" ", "+")
        origine_str = origine_str.upper()
        destination_str = str(destination).replace(" ", "+")
        destination_str = destination_str.upper()

        date_obj = datetime.strptime(date, '%d/%m/%Y')
        jour = str(date_obj.day)
        mois = str(date_obj.month)
        annee = str(date_obj.year)

        url = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.destination=" + destination_str + "&refine.date=" + annee + "%2F" + mois +  "%2F" + jour + "&refine.od_happy_card=" + eligible
     
        L=[]
        L.append(url)
        dict1 = rq.get(url)
        dict2=dict1.json()
        datatest=[dict2["records"][k]for k in range(len(dict2["records"]))]
        data=[datatest[k]['fields'] for k in range(len(dict2["records"]))]
        if len(data)==0:
            print("Aucun trajet correspond à votre recherche")
        else:
            for k in range(len(data)):
                print("Le train " + data[k]['train_no'] + " à destination de " + data[k]['destination'] + " partira de " + data[k]['origine'] + " à " +  data[k]['heure_depart'])
        return(L)

