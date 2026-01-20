from fastapi import APIRouter, HTTPException
from services import resolve_city_and_send

router = APIRouter()


@router.post("/")
def hhhhhh():
    try:
        return {"meseg":"hii"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

