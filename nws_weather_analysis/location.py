import pgeocode
from haversine import haversine

# Returns Latitude, Longitude for a given location (5-digit Zipcode OR City, State Code combination)
# pgeocode was used as it allows for both zipcode and city queries - documentation can be found here: https://pypi.org/project/pgeocode/
def get_lat_long(location):
    nomi = pgeocode.Nominatim('us')
    if(location.isnumeric()):
        if len(location) != 5:
            raise Exception(f"{location} is not a proper 5-digit Zipcode.")
        
        location_data = nomi.query_postal_code(location)
        if location_data.empty:
            raise Exception(f"No location data found for {location}, make sure to use a valid 5-digit Zipcode")
        
        latitude = location_data['latitude']
        longitude = location_data['longitude']
    else:
        city, state = split_city_state(location)
        city_data = nomi.query_location(city)
        location_data = city_data[city_data['state_code'] == state]
        if location_data.empty:
            raise Exception(f"No location data found for {location}, make sure to use a valid City, State Code combination (such as 'San Francisco, CA')")

        latitude = location_data['latitude'].iloc[0]
        longitude = location_data['longitude'].iloc[0]

        
    return latitude, longitude

def split_city_state(location):
        city, state = location.split(", ")
        return city, state
