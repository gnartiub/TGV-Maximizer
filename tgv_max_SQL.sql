/* création et gestion de la table utilisateur*/

/* création d'un compte*/
CREATE TABLE IF NOT EXISTS utilisateur (
                                id_user SERIAL PRIMARY KEY NOT NULL,
                                
                                mail VARCHAR(50),
                                MDP VARCHAR(50),
                                dateNaissance VARCHAR(50),
                                nom VARCHAR(50),
                                prenom VARCHAR(50)
                                );
INSERT INTO utilisateur (mail,MDP,dateNaissance, nom, prenom \
                    ) VALUES (%(mail)s, %(MDP)s, %(dateNaissance)s, %(nom)s, %(prenom)s) RETURNING id_user \
                    {
                    "MDP": user.MDP,
                    "mail": user.mail,
                    "nom": user.nom,
                    "prenom": user.prenom,
                    "dateNaissance": user.dateNaissance};
/*connexion*/
SELECT * FROM utilisateur \
                    WHERE utilisateur.mail = %(mail)s AND utilisateur.MDP = %(mdp)s\
                    {"mdp": MDP,
                    "mail": mail};
/*changement de mot de passe*/
UPDATE utilisateur \
                    SET mdp=%(mdp)s \
                    WHERE mail=%(mail)s RETURNING id_user;

/*création et gestion de la table trajet*/

/* cas d'une recherche trajet ou destination*/
CREATE TABLE  IF NOT EXISTS trajet( id_trajet SERIAL PRIMARY KEY NOT NULL,
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
INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)\
                    VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s),
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
                    "origine_iata": data[k]['origine_iata']};

/* cas d'une recherche week end*/

CREATE TABLE  IF NOT EXISTS trajet( id_trajet SERIAL PRIMARY KEY NOT NULL,
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
INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)\
                    VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s),
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
                    "origine_iata": dataa[k]['origine_iata']};
INSERT INTO trajet (date,
                                        origine,
                                        od_happy_card,
                                        train_no,
                                        heure_arrivee,
                                        axe,
                                        destination,
                                        entity,
                                        destination_iata,
                                        heure_depart,
                                        origine_iata)\
                    VALUES (%(date)s,
                                        %(origine)s,
                                        %(od_happy_card)s,
                                        %(train_no)s,
                                        %(heure_arrivee)s,
                                        %(axe)s,
                                        %(destination)s,
                                        %(entity)s,
                                        %(destination_iata)s,
                                        %(heure_depart)s,
                                        %(origine_iata)s),
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
                    "origine_iata": datar[k]['origine_iata']}

/* création et gestion de l'historique*/ 

CREATE TABLE IF NOT EXISTS historique( id_rech SERIAL PRIMARY KEY NOT NULL,
                                        type VARCHAR(40),
                                                                date VARCHAR(40),
                                                                origine VARCHAR(40),
                                                                destination VARCHAR(40),
                                                                eligible VARCHAR(40),
                                                                alerter VARCHAR(40));
INSERT INTO historique(type, date, origine, destination,
                                                eligible, alerter)
                VALUES(%(type)s,
                                %(date)s,
                                %(origine)s,
                                %(destination)s,
                                %(eligible)s,
                                %(alerter)s),
                    {"type": typerech,
                    "date" : date,
                    "origine" : origine,
                    "destination" : destination,
                    "eligible" : eligible,
                    "alerter" : alerter
                    }