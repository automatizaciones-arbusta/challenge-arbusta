import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- CONFIGURACIÓN DE BASE DE DATOS (OPCIONAL) ---
# Usaremos SQLite, que crea un archivo local. No requiere instalación extra.
DB_NAME = "feedback_db.sqlite"

def init_db():
    """
    Inicializa la base de datos.
    TODO (OPCIONAL - NIVEL 2): 
    Si decides hacer la parte de SQL, escribe aquí el código para:
    1. Conectar a SQLite.
    2. Crear la tabla 'feedback' si no existe.
       Columnas sugeridas: id (autoincremental), texto, sentimiento, es_correcto (bool).
    """
    pass 

app = FastAPI(title="Feedback AI API")

# Intentamos iniciar la DB al arrancar la app
init_db()

# --- MODELOS DE DATOS ---
class FeedbackRequest(BaseModel):
    texto: str

class FeedbackCorrection(BaseModel):
    id_registro: int
    es_correcto: bool

# --- TUS TAREAS A COMPLETAR ---

def analizar_sentimiento(texto: str) -> str:
    """
    TODO (OBLIGATORIO - NIVEL 1): 
    Implementa tu lógica de análisis aquí.
    Debe retornar: "Positivo", "Negativo" o "Neutral".
    
    Tip: Puedes empezar con algo simple (if/else) y luego mejorarlo.
    """
    # Escribe tu código aquí...
    return "Neutral"

@app.post("/analizar")
def predecir_feedback(request: FeedbackRequest):
    # 1. Ejecutar análisis (OBLIGATORIO)
    sentimiento = analizar_sentimiento(request.texto)
    
    # 2. Guardar en Base de Datos (OPCIONAL - NIVEL 2)
    # TODO: Si hiciste la parte SQL, guarda el texto y el resultado aquí.
    # Tip: Necesitarás recuperar el ID del registro creado (cursor.lastrowid) para retornarlo.
    id_guardado = 0 
    
    return {
        "status": "ok", 
        "texto_analizado": request.texto,
        "sentimiento": sentimiento, 
        "id_registro": id_guardado
    }

@app.post("/corregir")
def corregir_humano(correction: FeedbackCorrection):
    """
    Este endpoint es para el NIVEL 2 (Opcional).
    Sirve para que un humano diga si la IA acertó o no.
    """
    # TODO (OPCIONAL - NIVEL 2): 
    # Actualiza el campo 'es_correcto' en la base de datos usando el correction.id_registro.
    
    return {"status": "recibido", "mensaje": "Gracias por el feedback humano!"}

if __name__ == "__main__":
    import uvicorn
    print("Iniciando API... ve a http://localhost:8000/docs para probarla.")
    uvicorn.run(app, host="0.0.0.0", port=8000)
