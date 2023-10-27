import unittest
from unittest.mock import Mock
from nws_weather_analysis import station

class TestStationMethods(unittest.TestCase):
    def test_get_nearest_station_with_valid_data(self):
        # Test get_nearest_station with valid data
        point = (40.7128, -74.0060)  # New York City coordinates
        nearest_station = station.get_nearest_station(point)
        self.assertIsNotNone(nearest_station)

    def test_get_station_data(self):
        # Test get_station_data function
        station_data = station.get_station_data()
        self.assertIsNotNone(station_data)

    def test_get_station_id(self):
        # Test get_station_id function
        station_data = {
            'properties': {'stationIdentifier': '005PG'},
        }
        station_id = station.get_station_id(station_data)
        self.assertEqual(station_id, '005PG')

    def test_get_station_observation_data(self):
        # Test get_station_observation_data function
        station_id = '005PG'
        station_observation_data = station.get_station_observation_data(station_id)
        self.assertIsNotNone(station_observation_data)

    def test_get_station_observation_data_empty(self):
        # Mock a successful API response with empty features
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'features': []}

        # Mock the requests.get method to return the mock_response
        with unittest.mock.patch('requests.get', return_value=mock_response):
            with self.assertWarns(Warning):
                result = station.get_station_observation_data('station_id')

        self.assertEqual(result, {'features': []})

if __name__ == '__main__':
    unittest.main()
