import unittest
import pandas as pd
from nws_weather_analysis import weather


class TestWeatherMethods(unittest.TestCase):
    def test_get_temperature_data(self):
        # Create a mock station observation data
        observation_data = {
            'features': [
                {
                    'properties': {
                        'timestamp': '2023-10-27T12:00:00Z',
                        'temperature': {
                            'value': 20.5
                        }
                    }
                },
                {
                    'properties': {
                        'timestamp': '2023-10-26T12:00:00Z',
                        'temperature': {
                            'value': 25.0
                        }
                    }
                }
            ]
        }

        # Test get_temperature_data function with mock observation data
        temperature_df = weather.get_temperature_data(observation_data)
        self.assertIsInstance(temperature_df, pd.DataFrame)
        self.assertEqual(len(temperature_df), 2)
        self.assertEqual(list(temperature_df.columns), ['date', 'temperature_celsius'])
        self.assertAlmostEqual(temperature_df['temperature_celsius'].iloc[0], 20.5, places=2)
        self.assertAlmostEqual(temperature_df['temperature_celsius'].iloc[1], 25.0, places=2)

    def test_get_highs_and_lows(self):
        # Create a mock DataFrame with temperature data
        temperature_data = pd.DataFrame({
            'date': ['2023-10-27', '2023-10-27', '2023-10-26', '2023-10-26'],
            'temperature_celsius': [20.5, 18.5, 25.0, 15.0]
        })

        # Test get_highs_and_lows function with mock temperature data
        highs_lows_df = weather.get_highs_and_lows(temperature_data)
        self.assertIsInstance(highs_lows_df, pd.DataFrame)
        self.assertEqual(len(highs_lows_df), 2)
        self.assertAlmostEqual(highs_lows_df[('temperature_celsius', 'temperature_celsius_high')].iloc[0], 20.5, places=2)
        self.assertAlmostEqual(highs_lows_df[('temperature_celsius', 'temperature_celsius_low')].iloc[0], 18.5, places=2)
        self.assertAlmostEqual(highs_lows_df[('temperature_celsius', 'temperature_celsius_high')].iloc[1], 25.0, places=2)
        self.assertAlmostEqual(highs_lows_df[('temperature_celsius', 'temperature_celsius_low')].iloc[1], 15.0, places=2)

    def test_get_date_from_observation(self):
        # Create a mock observation with a timestamp
        observation = {
            'properties': {
                'timestamp': '2023-10-27T12:00:00Z'
            }
        }

        # Test get_date_from_observation function
        date = weather.get_date_from_observation(observation)
        self.assertEqual(date, '2023-10-27')

if __name__ == '__main__':
    unittest.main()
