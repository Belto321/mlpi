import pandas as pd
import os
from fastapi import HTTPException
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List

# Ruta absoluta del archivo CSV combinado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
movies_file = os.path.join(BASE_DIR, 'movies_combined.csv')

# Cargar el archivo CSV combinado
df_movies = pd.read_csv(movies_file)
df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')

# Cargar el archivo binario con los vectores de recomendación
with open(os.path.join(BASE_DIR, 'movie_vectors.pkl'), 'rb') as f:
    movie_vectors = pickle.load(f)

titles = movie_vectors["titles"]
tfidf_matrix = movie_vectors["tfidf_matrix"]

# Función para recomendaciones
def get_recommendations(titulo: str, n_recommendations: int = 5) -> List[str]:
    try:
        idx = np.where(titles == titulo)[0][0]
    except IndexError:
        raise HTTPException(status_code=404, detail=f"La película '{titulo}' no se encuentra en el dataset.")
    
    target_vector = tfidf_matrix[idx]
    sim_scores = cosine_similarity(target_vector, tfidf_matrix).flatten()
    sim_scores_indices = np.argsort(sim_scores)[::-1][1:n_recommendations+1]
    recommended_titles = [titles[i] for i in sim_scores_indices]
    return recommended_titles

# Funciones para los endpoints según la rúbrica

def cantidad_filmaciones_mes(mes: str):
    # Diccionario de meses en español a números de mes
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    
    # Verificar que el mes ingresado sea válido
    if mes.lower() not in meses:
        raise HTTPException(status_code=400, detail="Mes inválido.")
    
    # Filtrar el DataFrame por el mes deseado
    mes_num = meses[mes.lower()]
    count = df_movies[df_movies['release_date'].dt.month == mes_num].shape[0]
    
    return {"mensaje": f"{count} cantidad de películas fueron estrenadas en el mes de {mes}"}



def cantidad_filmaciones_dia(dia: str):
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    if dia.lower() not in dias:
        raise HTTPException(status_code=400, detail="Día inválido.")
    df_movies['release_date'] = pd.to_datetime(df_movies['release_date'], errors='coerce')
    count = df_movies[df_movies['release_date'].dt.day_name(locale='es').str.lower() == dia.lower()].shape[0]
    return {"mensaje": f"{count} cantidad de películas fueron estrenadas en los días {dia}"}

def score_titulo(titulo: str):
    film = df_movies[df_movies['title'].str.lower() == titulo.lower()]
    if film.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada.")
    title = film['title'].values[0]
    year = int(film['release_year'].values[0])
    score = film['vote_average'].values[0]
    return {"mensaje": f"La película {title} fue estrenada en el año {year} con un score de {score}"}

def votos_titulo(titulo: str):
    film = df_movies[df_movies['title'].str.lower() == titulo.lower()]
    if film.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada.")
    votes = film['vote_count'].values[0]
    if votes < 2000:
        return {"mensaje": "La película no cumple con la condición de tener al menos 2000 valoraciones."}
    title = film['title'].values[0]
    avg_vote = film['vote_average'].values[0]
    return {"mensaje": f"La película {title} tiene {votes} valoraciones con un promedio de {avg_vote}"}

def get_actor(nombre_actor: str):
    films = df_movies[df_movies['cast'].str.contains(nombre_actor, case=False, na=False)]
    if films.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado.")
    total_return = films['return'].sum()
    count = films.shape[0]
    avg_return = total_return / count if count > 0 else 0
    return {"mensaje": f"El actor {nombre_actor} ha participado en {count} filmaciones con un retorno total de {total_return} y un promedio de {avg_return} por filmación"}

def get_director(nombre_director: str):
    films = df_movies[df_movies['crew'].str.contains(nombre_director, case=False, na=False)]
    if films.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado.")
    film_list = []
    for _, row in films.iterrows():
        film_info = {
            "titulo": row['title'],
            "fecha_lanzamiento": row['release_date'].date(),
            "retorno": row['return'],
            "costo": row['budget'],
            "ganancia": row['revenue']
        }
        film_list.append(film_info)
    return {"director": nombre_director, "filmaciones": film_list}
