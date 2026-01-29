# 🚀 Desafío Técnico: The Intelligent Feedback API

¡Hola! Bienvenido al desafío técnico de **[Nombre de tu Empresa]**.

Si estás leyendo esto, es porque nos interesa tu perfil y queremos ver cómo piensas, cómo estructuras tu código y cómo resuelves problemas prácticos. No buscamos la "solución perfecta", sino código limpio, funcional y buena predisposición para aprender.

## 🎯 La Misión

En este repositorio encontrarás un archivo `main.py` con una API construida en **FastAPI**. El problema es que está incompleta.

Tu objetivo es rellenar los espacios marcados con `# TODO` para crear una API que pueda:
1.  Recibir un texto.
2.  Analizar si el sentimiento es **Positivo**, **Negativo** o **Neutral**.
3.  (Opcional) Guardar el resultado en una base de datos.
4.  (Opcional) Permitir que un humano corrija a la IA.

## 📝 Las Tareas

### Nivel 1: Obligatorio (El Core)
- [ ] **Lógica de Análisis:** Completa la función `analizar_sentimiento` en `main.py`. Puedes usar reglas simples (ej: `if "malo" in texto`) o investigar e integrar una librería de NLP (como TextBlob, NLTK, etc.).
- [ ] **Documentación:** Edita este `README.md` (o crea uno nuevo) explicando brevemente cómo ejecutar tu solución y qué librerías extra usaste (si usaste alguna).

### Nivel 2: Opcional (Suma Puntos ⭐)
Si te animas a ir más allá, intenta completar estos puntos:
- [ ] **Persistencia (SQL):** Completa la función `init_db` y la lógica dentro del endpoint `/analizar` para guardar los datos en **SQLite**.
- [ ] **Human-in-the-Loop:** Implementa el endpoint `/corregir`. Este endpoint debe permitir actualizar un registro en la base de datos si la predicción de la IA fue incorrecta.

## 🛠️ Cómo empezar

Sigue estos pasos para configurar tu entorno local:

1.  **Clona este repositorio** (o descárgalo):
    ```bash
    git clone <URL_DEL_REPO>
    cd <NOMBRE_CARPETA>
    ```

2.  **Prepara tu entorno (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el servidor:**
    ```bash
    python main.py
    ```

5.  **Prueba tu API:**
    Abre tu navegador y ve a: `http://localhost:8000/docs`. Verás la interfaz interactiva de Swagger para probar tus endpoints.

## 📦 Entrega

1.  Asegúrate de que tu código corra sin errores.
2.  Sube tu solución a tu propio repositorio de GitHub/GitLab (público) o comprímelo en un `.zip`.
3.  Envíanos el link o el archivo.

¡Muchos éxitos! Esperamos ver tu código.
