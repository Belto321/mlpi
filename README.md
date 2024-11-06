# API de Análisis de Películas

## Descripción

Esta es una API desarrollada con FastAPI para realizar consultas y análisis sobre un dataset de películas. Ofrece funcionalidades como contar la cantidad de películas estrenadas en un mes o día específico, obtener el puntaje de una película, y recomendaciones basadas en la similitud de títulos. El proyecto también incluye una interfaz de usuario sencilla (HTML, CSS y JavaScript) para interactuar con la API.

## Objetivos

- **Consultas de información**: Proporcionar detalles específicos sobre películas, como puntajes, cantidad de votos y más.
- **Análisis de datos**: Realizar análisis en función de días de estreno, meses, actores y directores.
- **Recomendaciones**: Ofrecer recomendaciones de películas similares basadas en la similitud de contenido.
- **Interfaz de Usuario**: Facilitar la interacción con la API mediante una página web simple.

## Estructura del Proyecto

La estructura del proyecto está organizada para permitir la fácil integración de la API y el frontend:

# mlpi
Proyecto individual de Machine learning  
mlpi/  
├── app/  
│ ├── functions.py # Funciones de la lógica de cada endpoint  
│ ├── main.py # Definición de la API con FastAPI  
│ ├── index.html # Interfaz de usuario para la API  
│ ├── movies_combined.csv # Dataset combinado con información de películas  
│ ├── movie_vectors.pkl # Archivo binario con vectores de recomendación  
└── requirements.txt # Dependencias del proyecto  

### Descripción de Archivos y Carpetas

- **`app/functions.py`**: Contiene las funciones que implementan la lógica de cada endpoint de la API. Aquí se procesan las consultas y se define la lógica de recomendación.
- **`app/main.py`**: Archivo principal de la API. Define los endpoints y conecta cada ruta con su función correspondiente en `functions.py`.
- **`app/index.html`**: Página HTML que sirve como interfaz de usuario. Permite realizar solicitudes a la API desde el navegador y muestra los resultados de manera dinámica.
- **`app/movies_combined.csv`**: Dataset combinado que contiene información detallada de las películas, como título, fecha de lanzamiento, puntaje, actores y directores.
- **`app/movie_vectors.pkl`**: Archivo binario con los vectores preprocesados necesarios para el sistema de recomendaciones.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar la API y el procesamiento de datos.

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/mlpi.git
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el servidor de FastAPI

```bash
uvicorn app.main:app --reload
```
La API estará disponible, accede a http://127.0.0.1:8000/ para ver la interfaz de usuario y comenzar a interactuar con la API.
