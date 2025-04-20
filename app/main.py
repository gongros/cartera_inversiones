from fastapi import FastAPI
from app.routes import grafico

app = FastAPI()
app.include_router(grafico.router)
