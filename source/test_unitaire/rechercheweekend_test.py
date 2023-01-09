import unittest
from recherche.recherchetrajet import RechercheTrajet

class TestRechercheWeekend(unittest.TestCase):
    
    def test_rechecheweekend(self):
        
        # GIVEN
        date_aller ="30/11/2022"
        origine = "Rennes"
        destination = "Lorient"
        objet = TestRechercheWeekend()
        
        
        # WHEN
        rec = objet.recherche(date_aller, origine, destination)
        
        # THEN
        self.assertEqual(rec, ['https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=RENNES&refine.destination=LORIENT&refine.date=2022%2F12%2F3&exclude.od_happy_card=OUI', 
                               'https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=LORIENT&refine.destination=RENNES&refine.date=2022%2F12%2F5&exclude.od_happy_card=OUI'])
                         
if __name__ == '__main__':
    unittest.main()