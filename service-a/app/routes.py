from fastapi import APIRouter, HTTPException
from services import resolve_city_and_send

router = APIRouter()


@router.post("/ingest")
def get_data_ingestion(location_name:str):

    try:
        data = resolve_city_and_send(location_name)
        return { "data": data }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

