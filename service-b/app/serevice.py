import pandas as pd
from pandas import DataFrame
import json

def create_data_frame(data):
    data = json.loads(data)
    return pd.DataFrame(data)

def config_typs_db(df:DataFrame):
    df["timestamp"]=pd.to_datetime(df["timestamp"])
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
