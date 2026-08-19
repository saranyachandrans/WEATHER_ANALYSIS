![](static/images/banner.png)
# WEATHER_ANALYSIS
Analyzed historical and recent weather data from 2022 to 2026 to identify trends and patterns in temperature, rainfall, humidity, and wind conditions.

### Directory Structure 
```tree
weather-data-analysis/
│
├── static/
│   └── raw/
│       └── thiruvananthapuram_weather_2022_2026.csv
│
├── config/
│   └── config.yml
│
├── src/
│   └── data_ingestion.py
│   └── datatransformation.py
│
└── .gitignore
│
└── .requirements.txt
```

## Weather Dataset Description

This project collects historical hourly weather data for **Thiruvananthapuram, Kerala, India** using the **Open-Meteo Historical Weather API**. The data is collected through a Python-based data ingestion pipeline, with API parameters such as location, date range, weather variables, timezone, and units managed through `config/config.yml`. The downloaded data is stored as a CSV file in `static/raw/`.

### Data Source

- **API:** Open-Meteo Historical Weather API
- **Location:** Thiruvananthapuram, Kerala, India
- **Latitude:** 8.5241
- **Longitude:** 76.9366
- **Time Period:** 2022-01-01 to 2026-08-18
- **Frequency:** Hourly
- **Timezone:** Asia/Kolkata
- **Temperature Unit:** °C
- **Wind Speed Unit:** km/h
- **Precipitation Unit:** mm

### Column Description

| Column | Description | Unit / Format |
|---|---|---|
| `time` | Date and time of the weather observation | YYYY-MM-DD HH:MM:SS |
| `temperature_2m` | Air temperature measured at 2 metres above the surface | °C |
| `relative_humidity_2m` | Relative humidity measured at 2 metres above the surface | % |
| `apparent_temperature` | Feels-like temperature considering temperature, humidity, wind and other factors | °C |
| `precipitation` | Total precipitation during the hour | mm |
| `rain` | Amount of rainfall during the hour | mm |
| `weather_code` | WMO weather code representing the weather condition | Numeric code |
| `cloud_cover` | Percentage of the sky covered by clouds | % |
| `surface_pressure` | Atmospheric pressure at the surface | hPa |
| `wind_speed_10m` | Wind speed measured at 10 metres above the surface | km/h |
| `wind_direction_10m` | Direction from which the wind is blowing at 10 metres | Degrees (°) |
| `wind_gusts_10m` | Maximum wind gust speed at 10 metres | km/h |

### Weather Code

The `weather_code` column follows the **WMO weather interpretation codes** used by Open-Meteo.

| Code | Weather Condition |
|---:|---|
| `0` | Clear sky |
| `1` | Mainly clear |
| `2` | Partly cloudy |
| `3` | Overcast |
| `45, 48` | Fog |
| `51–57` | Drizzle |
| `61–67` | Rain |
| `71–77` | Snow |
| `80–82` | Rain showers |
| `85–86` | Snow showers |
| `95` | Thunderstorm |
| `96, 99` | Thunderstorm with hail |

### Data Ingestion Process

1. API parameters are stored in `config/config.yml`.
2. The Python script reads the configuration using `PyYAML`.
3. A request is sent to the Open-Meteo Historical Weather API.
4. The hourly API response is converted into a Pandas DataFrame.
5. The `time` column is converted to datetime format.
6. The downloaded dataset is saved as a CSV file in `static/raw/`.

This configuration-driven approach keeps the **API settings separate from the Python code**, making it easier to modify the location, date range, weather variables, and output file without changing the ingestion logic.