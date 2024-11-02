import os
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import HTTPException
from typing import List

# Obtener la ruta absoluta al archivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'movie_vectors.pkl')

# Cargar los vectores y títulos desde el archivo binario al iniciar el servidor
with open(file_path, 'rb') as f:
    movie_vectors = pickle.load(f)

titles = movie_vectors["titles"]
tfidf_matrix = movie_vectors["tfidf_matrix"]

# Definir la función de recomendación
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
