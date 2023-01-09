from typing import List, Optional

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utilisateur.utilisateur import Utilisateur


class DAOprofil(metaclass=Singleton):
    ######################## CHANGER DE MAIL ######################
    def changer_mail(self,user , nouveau_mail):
        """
        Changer l'address mail de l'utilisateur

        Parametres:

            user: Utilisateur
            nouveau_mail: str

        Retourner:
            Bool (True si le mail est changé avec succès)
        """
        request=  "UPDATE utilisateur "\
                    "SET mail=%(mail)s"\
                    " WHERE mdp=%(mdp)s RETURNING id_user "
        connection=DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                request,
                {"mail":nouveau_mail,
                "mdp": user.MDP
                })
            res = cursor.fetchone()
        if res is not None :
            return True
        else :
            return False             


####################### CHANGER DE MOT DE PASSE #####################
    def changer_MDP(self,user , nouveau_mdp):
        """
        Changer le mot de passe de l'utilisateur

        Parametres:

            user: Utilisateur
            nouveau_mdp: str

        Retourner:
            Bool (True si le mdp est changé avec succès)
        """
        request=  "UPDATE utilisateur "\
                    "SET mdp=%(mdp)s "\
                    "WHERE mail=%(mail)s RETURNING id_user "  
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    request,
                    {"mdp":nouveau_mdp,
                    "mail":user.mail
                    })
                res = cursor.fetchone()
                print(res)
        if res is not None :
            return True
        else :
            return False                 



###################### CREER SON COMPTE #####################
    def creer_compte(self,user: Utilisateur):
        """
        Créer une compte d'utilisateur en ajoutant les informations Utilisateur dans le base de données

        Parametres:

            user: Utilisateur

        Retourner:
            created: Bool (True si la compte est créée avec succès)
        """
        created = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                create_script='''
                           CREATE TABLE IF NOT EXISTS utilisateur (
                                id_user SERIAL PRIMARY KEY NOT NULL,
                                
                                mail VARCHAR(50),
                                MDP VARCHAR(50),
                                dateNaissance VARCHAR(50),
                                nom VARCHAR(50),
                                prenom VARCHAR(50)
                                );'''
                                        
                cursor.execute(create_script)
                cursor.execute(
                    "INSERT INTO utilisateur (mail,MDP,dateNaissance, nom, prenom" \
                    ") VALUES (%(mail)s, %(MDP)s, %(dateNaissance)s, %(nom)s, %(prenom)s) RETURNING id_user"\
                    ,{
                    "MDP": user.MDP,
                    "mail": user.mail,
                    "nom": user.nom,
                    "prenom": user.prenom,
                    "dateNaissance": user.dateNaissance
                    })
                res = cursor.fetchone()
        if res:
            created = True
        else :
            created = False
        
        return created
        

            


###################### SE CONNECTER #####################
    def connexion(self,mail, MDP):
        """
        Utilisateur se connecte en utilisant son mail et mdp

        Parametres:

            mail: str
            mdp: str

        Retourner:
            user: Utilisateur
        """
        user = Utilisateur()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM utilisateur "\
                    "WHERE utilisateur.mail = %(mail)s AND utilisateur.MDP = %(mdp)s ",
                    {"mdp": MDP,
                    "mail": mail}
                    )
                res = cursor.fetchone()   
                
            
                 
        if res :
            user = Utilisateur(
                id  = res['id_user'],
                mail = res['mail'],
                prenom= res['prenom'],
                nom= res['nom'],
                MDP= res['mdp'],
                dateNaissance= res['datenaissance']
            )
            return user
        else : 
            return(0)

                               

###################### VERIFIER SI LE MAIL A ÉTÉ UTILISÉ #####################
    def verifier_mail(self,mail):
        """
        Cette fonction vérifie si l'adresse mail a été utilisé pour creer un compte

        Parametres:

            mail: str

        Retourner:
            used: Bool
        """
        used = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM utilisateur "\
                    "WHERE utilisateur.mail = %(mail)s",
                    {
                    "mail": mail}
                    )
                res = cursor.fetchall()   
                
            
                 
        if res :
            used = True
        else:
            used= False
        return used

                               






