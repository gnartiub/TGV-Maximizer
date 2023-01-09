import unittest
from recherche.recherchedestination import RechercheDestination

class TestRechercheDestination(unittest.TestCase):
    
    def test_rechechedestination(self):
        
        # GIVEN
        date ="30/11/2022"
        origine = "Rennes"
        objet = RechercheDestination()
        
        # WHEN
        rec = objet.recherche(date, origine)
        
        # THEN
        self.assertEqual(rec, ['https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=RENNES&refine.date=2022%2F11%2F30&exclude.od_happy_card=OUI'])

if __name__ == '__main__':
    unittest.main()