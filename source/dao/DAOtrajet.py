import psycopg2
import requests
import gzip
import json
from dao.db_connection import DBConnection

from utils.singleton import Singleton
class DAOTrajet():

    def DAOTrajet(self,url,typerech,date,origine,destination,eligible,alerter):
        """
        Remplir les trajets dans la table Trajet et les critères de recherche dans la table Historique de notre base
        Parametres:
            url: str
            typerech: str
            date: str de type dd/mm/yyyy
            origine: str
            destination: str
            eligible: str
            alerter: str
        Retourner:
            None
        """
        ### import d'un dictionnaire via l'API
        if typerech=="trajet" or typerech=="destination":
            dict1=requests.get(url[0])
            dict2=dict1.json()
            datatest=[dict2["records"][k]for k in range(len(dict2["records"]))]
            data=[datatest[k]['fields'] for k in range(len(dict2["records"]))]
            conn=None
            cur=None
        
            ###Connexion au serveur 
            conn = DBConnection().connection
            cur = conn.cursor()
        ###Creation de la table
            create_script='''CREATE TABLE  IF NOT EXISTS trajet( id_trajet SERIAL PRIMARY KEY NOT NULL,
                                        date VARCHAR(40),
                                        origine VARCHAR(40),
                                        od_happy_card VARCHAR(40),
                                        train_no VARCHAR(40),
                                        heure_arrivee VARCHAR(40) ,
                                        axe VARCHAR(40) ,
                                        destination VARCHAR(40),
                                        entity VARCHAR(40),
                                        destination_iata VARCHAR(40) ,
                                        heure_depart  VARCHAR(40),
                                        origine_iata   VARCHAR(40));
                        CREATE TABLE IF NOT EXISTS historique( id_rech SERIAL PRIMARY KEY NOT NULL,
                                        type VARCHAR(40),
                                                                date VARCHAR(40),
                                                                origine VARCHAR(40),
                                                                destination VARCHAR(40),
                                                                eligible VARCHAR(40),
                                                                alerter VARCHAR(40))'''
                                        
            cur.execute(create_script)
            cur.execute('''INSERT INTO historique(type, date, origine, destination,
                                                eligible, alerter)'''\
                    '''VALUES(%(type)s,
                                %(date)s,
                                %(origine)s,
                                %(destination)s,
                                %(eligible)s,
                                %(alerter)s)''',
                    {"type": typerech,
                    "date" : date,
                    "origine" : origine,
                    "destination" : destination,
                    "eligible" : eligible,
                    "alerter" : alerter
                    })
        ###Remplissage de la table
            for k in range(len(dict2["records"])):
                cur.execute('''INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)'''\
                    '''VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s)''',
                    {"date": data[k]['date'],
                    "origine" : data[k]['origine'],
                    "od_happy_card": data[k]['od_happy_card'],
                    "train_no": data[k]['train_no'],
                    "heure_arrivee": data[k]['heure_arrivee'],
                    "axe": data[k]['axe'],
                    "destination": data[k]['destination'],
                    "entity": data[k]['entity'],
                    "destination_iata": data[k]['destination_iata'],
                    "heure_depart": data[k]['heure_depart'],
                    "origine_iata": data[k]['origine_iata']})
            
            conn.commit()

        
        
        
        if typerech=="weekend":
            dict1a=requests.get(url[0])
            dict2a=dict1a.json()
            dict1r=requests.get(url[1])
            dict2r=dict1r.json()
            data1a=[dict2a["records"][k]for k in range(len(dict2a["records"]))]
            dataa=[data1a[k]['fields'] for k in range(len(dict2a["records"]))]
            data1r=[dict2r["records"][k]for k in range(len(dict2r["records"]))]
            datar=[data1r[k]['fields'] for k in range(len(dict2r["records"]))]
            conn=None
            cur=None
            
            ###Connexion au serveur 
            conn = DBConnection().connection
            cur = conn.cursor()
        ###Creation de la table
            create_script='''CREATE TABLE  IF NOT EXISTS trajet( id_trajet SERIAL PRIMARY KEY NOT NULL,
                                        date VARCHAR(40),
                                        origine VARCHAR(40),
                                        od_happy_card VARCHAR(40),
                                        train_no VARCHAR(40),
                                        heure_arrivee VARCHAR(40) ,
                                        axe VARCHAR(40) ,
                                        destination VARCHAR(40),
                                        entity VARCHAR(40),
                                        destination_iata VARCHAR(40) ,
                                        heure_depart  VARCHAR(40),
                                        origine_iata   VARCHAR(40));
                        CREATE TABLE IF NOT EXISTS historique( id_rech SERIAL PRIMARY KEY NOT NULL,
                                        type VARCHAR(40),
                                                                date VARCHAR(40),
                                                                origine VARCHAR(40),
                                                                destination VARCHAR(40),
                                                                eligible VARCHAR(40),
                                                                alerter VARCHAR(40))'''
                                        
            cur.execute(create_script)
            cur.execute('''INSERT INTO historique(type, date, origine, destination,
                                                eligible, alerter)'''\
                    '''VALUES(%(type)s,
                                %(date)s,
                                %(origine)s,
                                %(destination)s,
                                %(eligible)s,
                                %(alerter)s)''',
                    {"type": typerech,
                    "date" : date,
                    "origine" : origine,
                    "destination" : destination,
                    "eligible" : eligible,
                    "alerter" : alerter
                    })
        ###Remplissage de la table
            for k in range(len(dict2a["records"])):
                cur.execute('''INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)'''\
                    '''VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s)''',
                    {"date": dataa[k]['date'],
                    "origine" : dataa[k]['origine'],
                    "od_happy_card": dataa[k]['od_happy_card'],
                    "train_no": dataa[k]['train_no'],
                    "heure_arrivee": dataa[k]['heure_arrivee'],
                    "axe": dataa[k]['axe'],
                    "destination": dataa[k]['destination'],
                    "entity": dataa[k]['entity'],
                    "destination_iata": dataa[k]['destination_iata'],
                    "heure_depart": dataa[k]['heure_depart'],
                    "origine_iata": dataa[k]['origine_iata']})
            for k in range(len(dict2r["records"])):
                cur.execute('''INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)'''\
                    '''VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s)''',
                    {"date": datar[k]['date'],
                    "origine" : datar[k]['origine'],
                    "od_happy_card": datar[k]['od_happy_card'],
                    "train_no": datar[k]['train_no'],
                    "heure_arrivee": datar[k]['heure_arrivee'],
                    "axe": datar[k]['axe'],
                    "destination": datar[k]['destination'],
                    "entity": datar[k]['entity'],
                    "destination_iata": datar[k]['destination_iata'],
                    "heure_depart": datar[k]['heure_depart'],
                    "origine_iata": datar[k]['origine_iata']})
            
            conn.commit()
    