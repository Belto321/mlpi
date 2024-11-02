from fastapi import FastAPI
from .functions import get_recommendations

# Inicializar la aplicación de FastAPI
app = FastAPI()

# Definir el endpoint para obtener recomendaciones
@app.get("/recomendacion")
async def recomendacion(titulo: str):
    recommendations = get_recommendations(titulo)
    return {"titulo": titulo, "recomendaciones": recommendations}
