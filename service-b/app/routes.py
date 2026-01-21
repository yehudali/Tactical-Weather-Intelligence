from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.post("/clean")
def hhhhhh():
    try:
        return {"meseg":"hii"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

