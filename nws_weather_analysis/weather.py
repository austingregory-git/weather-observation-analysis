import pandas as pd
import warnings

def get_temperature_data(station_observation_data):
    temperature_data = []
    for observation in station_observation_data['features']:
        date = get_date_from_observation(observation)
        temperature = observation['properties']['temperature']['value']
        temperature_data.append((date, temperature))
    df = pd.DataFrame(temperature_data, columns=['date', 'temperature_celsius'])
    df = df.dropna()

    # Note: many observations have a null value for temperature.value
    if df.empty:
        warnings.warn("No available observation data.")
    return df

# Get highs and lows for each date
# Resulting Dataframe has columns: 'date', 'temperature_celsius_high', 'temperature_celsius_low'
# Could easily convert to fahrenheit if needed. Important to specify temperature type in weather data.
# Opted to use pandas as it would be my primary choice if I were to push this into a database. If using spark, we could use PySpark dataframes
def get_highs_and_lows(df):
    df = df.groupby('date').agg({'temperature_celsius': [('temperature_celsius_high', 'max'), ('temperature_celsius_low', 'min')]})
    df = df.sort_values(by='date', ascending=False)
    return df

def get_date_from_observation(observation):
    timestamp = observation['properties']['timestamp']
    date = timestamp[:10]
    return date