from fastapi import FastAPI
from app.Routes import crud


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

app.include_router(crud.crudOperation)
app.include_router(crud.get_crudOperation)
