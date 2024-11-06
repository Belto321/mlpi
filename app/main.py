from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from .functions import (
    cantidad_filmaciones_mes,
    cantidad_filmaciones_dia,
    score_titulo,
    votos_titulo,
    get_actor,
    get_director,
    get_recommendations
)

app = FastAPI()

# Ruta para servir el archivo HTML en la raíz
@app.get("/")
def read_root():
    return FileResponse("app/index.html") 

@app.get("/recomendacion")
async def recomendacion(titulo: str):
    recommendations = get_recommendations(titulo)
    return {"titulo": titulo, "recomendaciones": recommendations}

@app.get("/cantidad_filmaciones_mes")
async def cantidad_filmaciones_mes_endpoint(mes: str):
    result = cantidad_filmaciones_mes(mes)
    return result

@app.get("/cantidad_filmaciones_dia")
async def cantidad_filmaciones_dia_endpoint(dia: str):
    result = cantidad_filmaciones_dia(dia)
    return result

@app.get("/score_titulo")
async def score_titulo_endpoint(titulo: str):
    result = score_titulo(titulo)
    return result

@app.get("/votos_titulo")
async def votos_titulo_endpoint(titulo: str):
    result = votos_titulo(titulo)
    return result

@app.get("/get_actor")
async def get_actor_endpoint(nombre_actor: str):
    result = get_actor(nombre_actor)
    return result

@app.get("/get_director")
async def get_director_endpoint(nombre_director: str):
    result = get_director(nombre_director)
    return result
