from datetime import datetime, timedelta
from recherche.abstractrecherche import AbstractRecherche
from datetime import datetime
import requests as rq

class RechercheWeekend(AbstractRecherche):
    
    def recherche(self,date, origine, destination, alerter , eligible):
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
        date_obj_aller = datetime.strptime(date, '%d/%m/%Y')
        date_obj_retour = date_obj_aller + timedelta(days = 2)

        jour_aller = str(date_obj_aller.day)
        mois_aller = str(date_obj_aller.month)
        annee_aller = str(date_obj_aller.year)
        jour_retour = str(date_obj_retour.day)
        mois_retour = str(date_obj_retour.month)
        annee_retour = str(date_obj_retour.year)

        url_aller = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.destination=" + destination_str + "&refine.date=" + annee_aller + "%2F" + mois_aller +  "%2F" + jour_aller + "&exclude.od_happy_card=" + eligible
        url_retour = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + destination_str + "&refine.destination=" +  origine_str + "&refine.date=" + annee_retour + "%2F" + mois_retour +  "%2F" + jour_retour + "&exclude.od_happy_card=" + eligible
        
        L=[]
        L.append(url_aller)
        L.append(url_retour)
        
        dict_aller = rq.get(url_aller)
        dict_aller = dict_aller.json()
        datatest_aller=[dict_aller["records"][k]for k in range(len(dict_aller["records"]))]
        data_aller=[datatest_aller[k]['fields'] for k in range(len(dict_aller["records"]))]
        dict_retour = rq.get(url_retour)
        dict_retour = dict_retour.json()
        datatest_retour = [dict_retour["records"][k]for k in range(len(dict_retour["records"]))]
        data_retour=[datatest_retour[k]['fields'] for k in range(len(dict_retour["records"]))]
        
        for k in range(min(len(data_aller),len(data_retour))):
            print("Le train aller" + data_aller[k]['train_no'] + " à destination de " + data_aller[k]['destination'] + " partira de " + data_aller[k]['origine'] + " à " +  data_aller[k]['heure_depart'])
        for k in range(min(len(data_aller),len(data_retour))):
                print("Le train retour" + data_retour[k]['train_no'] + " à destination de " + data_retour[k]['destination'] + " partira de " + data_retour[k]['origine'] + " à " +  data_retour[k]['heure_depart'])
        return(L) 

