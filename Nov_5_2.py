import unittest
from Nov_5_1 import city_f
class ctiytestcase(unittest.TestCase):

    def test_city_country(self):
        cf=city_f('santiago','chile')
        self.assertEqual(cf,'Santiago,Chile')

    def test_city_population(self):
        cf=city_f('santiago','chile',500)
        self.assertEqual(cf,'Santiago,Chile-population 500')

if __name__=='__main__':
    unittest.main()

