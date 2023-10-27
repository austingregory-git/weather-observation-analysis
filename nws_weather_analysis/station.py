import requests
import warnings
from haversine import haversine

# Get the nearest station given a point
# Basically find the lat/longs for each station and get the smallest distance to the given point using calculate_haversine_distance()
def get_nearest_station(point):
    station_data = get_station_data()
    nearest_station = None
    min_distance = float('inf')
    for station in station_data['features']:
        # Note: station data has latitude second
        latitude = station['geometry']['coordinates'][1]
        longitude = station['geometry']['coordinates'][0]
        station_point = (latitude, longitude)
        distance = calculate_haversine_distance(point, station_point)
        if distance < min_distance:
            min_distance = distance
            nearest_station = station

    return nearest_station

# Get all stations using National Weather Service api
def get_station_data():
    station_url = f"https://api.weather.gov/stations"
    station_response = requests.get(station_url)
    if station_response.status_code == 200:
        station_data = station_response.json()
        return station_data
    else:
        raise Exception(f"Failed to get station data from {station_url}. Status code: {station_response.status_code}")

def get_station_id(station):
    return station['properties']['stationIdentifier']

def get_station_observation_data(station_id):
    station_url = f"https://api.weather.gov/stations/{station_id}/observations"
    station_response = requests.get(station_url)
    if station_response.status_code == 200:
        station_data = station_response.json()

        # Note: many stations do not have any observation data at the current moment (Try 'Denver, CO' as an example - verify here: 'https://api.weather.gov/stations/07MT/observations')
        if len(station_data['features']) == 0:
            warnings.warn(f"No observation data found for station: {station_id}. You may verify this by visiting 'https://api.weather.gov/stations/{station_id}/observations'")
        return station_data
    else:
        raise Exception(f"Failed to get station data from {station_url}. Status code: {station_response.status_code}")

# Here I opted to use a python library to calculate the haversine distance (essentially the distance between two points on a sphere)
# For additional information about the formula, visit: https://en.wikipedia.org/wiki/Haversine_formula
# For documentation on the haversine library in python, visit: https://pypi.org/project/haversine/
def calculate_haversine_distance(point1, point2):
    return haversine(point1, point2)
