from fastapi import FastAPI
from app.routes import pydanticPostApi

app = FastAPI()

@app.get("/")
async def root():
    return { "message":"server started"}

app.include_router(pydanticPostApi.userData)