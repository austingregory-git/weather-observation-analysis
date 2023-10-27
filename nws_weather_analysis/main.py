from location import get_lat_long
from station import get_nearest_station, get_station_id, get_station_observation_data
from weather import get_temperature_data, get_highs_and_lows
import pandas as pd

def main():
    # Since the primary goal of this project is to display the relevant weather data, we can toggle these pandas display options
    # Not advised if there was more historical data, but in this case most observation stations that I checked only have ~10 days of data available 
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Print all available highs and lows in San Francisco
    print(get_highs_and_lows_from_location("San Francisco, CA"))

    # Print all available highs and lows at Zipcode (Charlotte, NC)
    print(get_highs_and_lows_from_location("28105"))

    # Print all available highs and lows in Denver (currently no observation data available, warning should be expected)
    print(get_highs_and_lows_from_location("Denver, CO"))

# Master Function to get all available highs and lows for each day given a location (5-digit zipcode OR City, State Code combination)
def get_highs_and_lows_from_location(location):
    point = get_lat_long(location)
    station = get_nearest_station(point)
    station_id = get_station_id(station)
    station_observation_data = get_station_observation_data(station_id)
    temperature_data = get_temperature_data(station_observation_data)
    highs_and_lows = get_highs_and_lows(temperature_data)
    return highs_and_lows


if __name__ == "__main__":
    main()