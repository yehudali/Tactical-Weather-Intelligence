import pandas as ps
from pandas import DataFrame

data = [
  {
    "timestamp": "2026-01-19T00:00:00",
    "location_name": "London",
    "country": "United Kingdom",
    "latitude": 51.50853,
    "longitude": -0.12574,
    "temperature": 8.6,
    "wind_speed": 3.9,
    "humidity": 83
  },
  {
    "timestamp": "2026-01-19T01:00:00",
    "location_name": "London",
    "country": "United Kingdom",
    "latitude": 51.50853,
    "longitude": -0.12574,
    "temperature": 8.2,
    "wind_speed": 3.4,
    "humidity": 84
  },
  {
    "timestamp": "2026-01-19T02:00:00",
    "location_name": "London",
    "country": "United Kingdom",
    "latitude": 51.50853,
    "longitude": -0.12574,
    "temperature": 8.1,
    "wind_speed": 3.1,
    "humidity": 84
  },
  {
    "timestamp": "2026-01-19T03:00:00",
    "location_name": "London",
    "country": "United Kingdom",
    "latitude": 51.50853,
    "longitude": -0.12574,
    "temperature": 8.1,
    "wind_speed": 12.6,
    "humidity": 86
  },
  {
    "timestamp": "2026-01-19T04:00:00",
    "location_name": "London",
    "country": "United Kingdom",
    "latitude": 51.50853,
    "longitude": -0.12574,
    "temperature": 20.1,
    "wind_speed": 3.9,
    "humidity": 89
  }]

df= ps.DataFrame(data)

def create_data_frame(data):
    return ps.DataFrame(data)

def config_typs_db(df:DataFrame):
    df["timestamp"]=df["timestamp"].astype("datetime64[ns]")
    df["location_name"] = df["location_name"].astype("category")
    df["country"] = df["country"].astype("category")
    return df

def create_temperature_category_colum(df:DataFrame):
    df["temperature_category"] = df["temperature"].apply(lambda x: "cold" if x < 19 else "moderate"  if x < 26 else "hot")
    return df

def auxiliary_function(num:float|int):
    if num > 9 :
        return "windy"
    else:
        return "calm"
    
def create_wind_status_colum(df: DataFrame):
    df["wind_status"] = df["wind_speed"].apply(auxiliary_function)
    return df
