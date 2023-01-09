# TGVMaximiser

TGVMaximiser is a train travel search application which allows you to save a lot of time by offering you directly the trains compatible with your SNCF MAX subscription.

For example, you decide to leave Rennes for Paris on December 19, 2022? You just have to enter the corresponding information in our application and it will give you the eligible trains.

## Installation

### Using the code

You can launch our application by running our main.py available in the root of our source file.

### Using the python intepreter

If you don't have access to our folder and you have a installation of Python and pip on your system, you can use it to run TGVMaximiser from the source:

```
git clone https://github.com/leonardgst/Projet-info.git
cd Projet-info
cd source
python main.py
```

Please, be sure to check the requirement.txt to make sure that you have all the packages needed.
Since the application depends on InquirerPy, it is recommended to use a virtual environment (venv) to run it with this method.

## Configuration

TGVMaximiser offers an easy-to-use interface that will allow you to register or log in, and then search for your trip whether you are looking for a specific trip, a destination or a weekend round trip. Then enter the requested information and the application will give you the trains eligible for your subscription.

For example, here a test of a connexion:

```

Bonjour
? Bienvenue à TGVMaximiser! 
>>> Se connecter
CONNEXION

? Quel est votre mail ?
>>> test@testmail.com 
? Quel est votre MDP ? 
>>> Test
```

This create an account for the user.
Now, this is an example of a request for a week-end trip from Rennes to Brest:

```

? Votre gare de départ: 
>>> rennes
? Votre gare d'arrivé:
>>> brest
? Choisir votre date de départ (sous forme dd/mm/yyyy): 
>>> 25/11/2022
? Etre alerté?(OUI/NON): 
>>>NON
? Place elligibles au TGVMax?(OUI/NON)
>>> OUI

Le train aller 8609 à destination de BREST partira de RENNES à 11:29
Le train retrour 8646 à destination de RENNES partira de BREST à 19:18

```

## Licence

This project is distributed under the terms of the [European Union Public License v. 1.2](https://eupl.eu/1.2/fr/).

The data of the SNCF API are used under the conditions of the [Open License](https://github.com/etalab/licence-ouverte).

