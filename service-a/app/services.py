import requests
from datetime import datetime

SERVICE_B_URL = "http://127.0.0.1:8001"
# --------- Helper: Geocoding ----------
def fetch_coordinates(location_name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": location_name,
        "count": 1
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError(f"Location not found: {location_name}")

    result = data["results"][0]
    return {
        "location_name": result["name"],
        "country": result.get("country"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


# --------- Helper: Weather ----------
def fetch_hourly_weather(latitude: float, longitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "past_days": 1,
        "timezone": "UTC"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["hourly"]


# --------- Main Ingestion Logic ----------
def ingest_weather_for_location(location_name: str) -> list[dict]:
    records = []


    # 1. Get coordinates
    location = fetch_coordinates(location_name)

    # 2. Get weather data
    hourly_data = fetch_hourly_weather(
        location["latitude"],
        location["longitude"]
    )

    times = hourly_data["time"]
    temperatures = hourly_data["temperature_2m"]
    wind_speeds = hourly_data["wind_speed_10m"]
    humidities = hourly_data["relative_humidity_2m"]

    # 3. Flatten to records (ONE record per hour per location)
    for i in range(len(times)):
        record = {
            "timestamp": times[i],
            "location_name": location["location_name"],
            "country": location["country"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "temperature": temperatures[i],
            "wind_speed": wind_speeds[i],
            "humidity": humidities[i]

        }
        records.append(record)

    return records

def send_to_service_b(weather_data: list[dict]):
    response = requests.post(
        f"{SERVICE_B_URL}/clean",
        json=weather_data
    )

    if not response.ok:
        raise Exception("failed to send data to service B")

    return response.json()

def resolve_city_and_send(location_name: str):
    weather_data = ingest_weather_for_location(location_name)
    result = send_to_service_b(weather_data)
    return result








