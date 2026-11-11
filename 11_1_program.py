import unittest
from city_function import city_country


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        hasil = city_country('santiago', 'chile')
        self.assertEqual(hasil, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
