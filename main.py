from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(title="Insurance Calculator API")
app.include_router(router)