from fastapi import APIRouter, HTTPException
from serevice import create_data_frame,config_typs_db, create_temperature_category_colum, create_wind_status_colum

router = APIRouter()


@router.post("/clean")
def Normalization_data_and_post_dataframe_for_servic_c(data):
    try:    
        df = create_data_frame(data)
        df = config_typs_db(df)
        df = create_temperature_category_colum(df)
        df = create_wind_status_colum(df)
        return {"meseg":df.to_json()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

