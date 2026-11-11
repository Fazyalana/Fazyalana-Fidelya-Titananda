
import unittest
from city_functions2 import city_country


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        hasil = city_country('santiago', 'chile')
        self.assertEqual(hasil, 'Santiago, Chile')

    def test_city_country_population(self):
        hasil = city_country(
            'santiago',
            'chile',
            populasi='5000000'
        )
        self.assertEqual(
            hasil,
            'Santiago, Chile - population 5000000'
        )


if __name__ == '__main__':
    unittest.main()
