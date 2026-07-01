from fastapi import FastAPI
from get_routes import router

app = FastAPI()

app.include_router(router)