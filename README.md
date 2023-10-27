# Weather Observation Analysis

## Overview

Weather Observation Analysis is a Python project that allows you to retrieve and analyze weather data from the National Weather Service (NWS) API. It provides functions to obtain weather observations, calculate temperatures (specifically highs and lows for each day from a station), and find the nearest weather station to a given point.

## Features

- Get weather observations from NWS stations.
- find temperature highs and lows for a given location (5-digit zipcodes OR City, State Code combinations (ie 'San Francisco, CA')).
- Find the nearest weather station based on coordinates.

## Installation

1. Clone the project repository to your local machine:

    ```shell
    git clone https://github.com/austingregory-git/weather-observation-analysis.git

    cd nws-weather-analysis

    pip install -r requirements.txt

## Usage

1. Open main.py and configure it to your needs
2. Run the script: 
    ```shell 
    python main.py

## Testing

1. Return to project directory (weather-observation-analysis): 
    ```shell
    cd ..
2. Run tests: 
    ```shell
    py -m unittest discover tests

## Dependencies

1. pgeocode: Python library for geocoding and reverse geocoding based on Nominatim.
2. pandas: Powerful data manipulation and analysis library.
3. haversine: Calculate the distance between two points on the Earth.
4. requests: HTTP library for making API requests.