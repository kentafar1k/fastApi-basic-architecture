from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/test")
async def test_api():
    try:
        return {"message": "API работает!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))