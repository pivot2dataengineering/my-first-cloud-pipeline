import requests
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import os
import json
# Load environment variables from .env file.
# My API key is held in a file named ".env", I use load_dotenv to pull the variable in for me
# This allows me to share working code on Github without exposing my actual API Key
# load_dotenv()
# API_KEY = os.getenv("API_KEY")


### MAKING REST API CALL TO GET DATA

# Replace YOUR_API_KEY with your actual API key
# TODO: REPLACE API KEY FROM https://www.weatherapi.com/my/
API_KEY = "ENTER_API_KEY_HERE"  # eg: API_KEY = "12343abb334sa"


def get_weather_data(start_date: str,
                     end_date: str,
                     location: str) -> json:
    """Uses API call to get weather data

    Returns:
        pd.DataFrame: DataFrame containing weather data
    """
    # Set the API endpoint URL
    url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={location}&dt={start_date}&end_dt={end_date}"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        return data
    else:
        raise ImportError(f"Error: {response.status_code} - {response.text}")

def parse_weather_data(data: json,
                       start_date: str,
                       end_date: str) -> pd.DataFrame:
        ### TRANSFORM PHASE - PARSING DATA FROM API CALL
        # Initialize an empty list to store weather data
        weather_data = []

        # Access the weather data
        location = data["location"]
        print(f"Location: {location['name']}, {location['region']}, {location['country']}")

        day_count = datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")
        print(day_count.days)

        for i in range(day_count.days):
            print(i)
            forecast = data["forecast"]["forecastday"][i]
            date = forecast["date"]
            print(f"Date: {date}")

            day = forecast["day"]
            max_temp = day["maxtemp_c"]
            min_temp = day["mintemp_c"]
            avg_temp = day["avgtemp_c"]
            precipitation = day["totalprecip_mm"]
            print(f"Maximum Temperature: {max_temp}°C")
            print(f"Minimum Temperature: {min_temp}°C")
            print(f"Average Temperature: {avg_temp}°C")
            print(f"Total Precipitation: {precipitation} mm")
            # Append the weather data to the list
            weather_data.append(
                {
                    "DATE": date, 
                    "MAX_TEMP": max_temp,
                    "MIN_TEMP": min_temp,
                    "AVG_TEMP": avg_temp,
                    "TOTAL_PRECIPITATION": precipitation,
                }
            )

        # Create a Pandas DataFrame from the weather data list
        weather_df = pd.DataFrame(weather_data)
        weather_df["DATE"] = pd.to_datetime(weather_df['DATE'], format='%Y-%m-%d')

        # Print the DataFrame
        print(weather_df)
        return weather_df


# Run the function locally to get weather data
if __name__ == "__main__":
    #TODO: setting date ranges
    temp_start_date = "2024-04-01"
    temp_end_date = "2024-04-30"
    #TODO: setting location
    temp_location = "Melbourne"
    actual = get_weather_data(
                    start_date=temp_start_date,
                    end_date=temp_end_date,
                    location=temp_location)
    parse_weather_data(actual, temp_start_date, temp_end_date)