from fastapi import APIRouter, HTTPException
from serevice import create_data_frame,config_typs_db, create_temperature_category_colum, create_wind_status_colum, manage_dataframe, sent_to_ander_service

router = APIRouter()


@router.post("/clean")
def Normalization_data_and_post_dataframe_for_servic_c(data):
    try:   
        df = manage_dataframe(data)
        sent_to_ander_service(df)
        return {"maseg": "ok"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

