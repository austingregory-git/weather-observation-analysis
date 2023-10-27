import unittest
from nws_weather_analysis import location

class TestLocationMethods(unittest.TestCase):
    def test_get_lat_long_with_valid_zipcode(self):
        # Test get_lat_long with a valid ZIP code (e.g., '77001')
        latitude, longitude = location.get_lat_long('77001')
        self.assertAlmostEqual(latitude, 29.8131, places=2)  # Expected latitude for ZIP code 77001
        self.assertAlmostEqual(longitude, -95.3098, places=2)  # Expected longitude for ZIP code 77001

    def test_get_lat_long_with_valid_city_state(self):
        # Test get_lat_long with a valid city/state location (e.g., 'San Francisco, CA')
        latitude, longitude = location.get_lat_long('San Francisco, CA')
        self.assertAlmostEqual(latitude, 37.7813, places=2)  # Expected latitude for San Francisco, CA
        self.assertAlmostEqual(longitude, -122.4167, places=2)  # Expected longitude for San Francisco, CA

    def test_get_lat_long_with_invalid_zipcode(self):
        # Test get_lat_long with an invalid ZIP code
        with self.assertRaises(Exception):
            location.get_lat_long('1234')

    def test_get_lat_long_with_invalid_city_state(self):
        # Test get_lat_long with an invalid city/state location
        with self.assertRaises(Exception):
            location.get_lat_long('NonExistentCity, NEC')

    def test_split_city_state(self):
        # Test split_city_state function
        city, state = location.split_city_state('Houston, TX')
        self.assertEqual(city, 'Houston')
        self.assertEqual(state, 'TX')

        city, state = location.split_city_state('Los Angeles, CA')
        self.assertEqual(city, 'Los Angeles')
        self.assertEqual(state, 'CA')

if __name__ == '__main__':
    unittest.main()

