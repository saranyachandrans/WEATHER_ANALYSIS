import requests
import pandas as pd
import yaml
from pathlib import Path


# ---------------------------------------
# Load configuration
# ---------------------------------------

config_path = Path("config/config.yml")

with open(config_path, "r") as file:
    config = yaml.safe_load(file)


# ---------------------------------------
# Read API configuration
# ---------------------------------------

url = config["api"]["url"]


# ---------------------------------------
# Read location parameters
# ---------------------------------------

latitude = config["location"]["latitude"]
longitude = config["location"]["longitude"]


# ---------------------------------------
# Read date range
# ---------------------------------------

start_date = config["date_range"]["start_date"]
end_date = config["date_range"]["end_date"]


# ---------------------------------------
# Read weather parameters
# ---------------------------------------

weather_config = config["weather"]

hourly_variables = weather_config["hourly"]
timezone = weather_config["timezone"]

temperature_unit = weather_config["temperature_unit"]
wind_speed_unit = weather_config["wind_speed_unit"]
precipitation_unit = weather_config["precipitation_unit"]


# ---------------------------------------
# Create API parameters
# ---------------------------------------

params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": start_date,
    "end_date": end_date,
    "hourly": hourly_variables,
    "timezone": timezone,
    "temperature_unit": temperature_unit,
    "wind_speed_unit": wind_speed_unit,
    "precipitation_unit": precipitation_unit
}


# ---------------------------------------
# Send API request
# ---------------------------------------

print("Downloading weather data...")

response = requests.get(url, params=params)

response.raise_for_status()

data = response.json()


# ---------------------------------------
# Convert JSON to DataFrame
# ---------------------------------------

df = pd.DataFrame(data["hourly"])


# ---------------------------------------
# Convert time column
# ---------------------------------------

df["time"] = pd.to_datetime(df["time"])


# ---------------------------------------
# Create output directory
# ---------------------------------------

output_directory = Path(config["output"]["directory"])

output_directory.mkdir(
    parents=True,
    exist_ok=True
)


# ---------------------------------------
# Save data
# ---------------------------------------

output_file = output_directory / config["output"]["filename"]

df.to_csv(output_file, index=False)


# ---------------------------------------
# Display information
# ---------------------------------------

print("\nData downloaded successfully!")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")
print(f"Saved to: {output_file}")

print("\nFirst 5 rows:")
print(df.head())