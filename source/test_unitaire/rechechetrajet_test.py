import unittest
from recherche.recherchetrajet import RechercheTrajet

class TestRechercheTrajet(unittest.TestCase):
    
    def test_rechechedestination(self):
        
        # GIVEN
        date ="30/11/2022"
        origine = "Rennes"
        objet = RechercheTrajet()
        destination = "Lorient"
        
        # WHEN
        rec = objet.recherche(date, origine, destination)
        
        # THEN
        self.assertEqual(rec, ['https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=RENNES&refine.destination=LORIENT&refine.date=2022%2F11%2F30&refine.od_happy_card=OUI'])

if __name__ == '__main__':
    unittest.main()