# 11-1

import unittest
from city_country import city_functions

class TestCity(unittest.TestCase):

    def test_city_country(self):
        """11-1 Testing city and country"""
        city_country = city_functions('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """11-2 Testing population"""
        describe_city = city_functions('santiago', 
                                       'chile', 500000)
        self.assertEqual(describe_city,
                          'Santiago, Chile -Population 500000')

unittest.main()