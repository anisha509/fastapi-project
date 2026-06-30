from fastapi import FastAPI 

router = APIRouter()

@router.get("/hello")
def get_data():
    return {"message": "GET method working"}

