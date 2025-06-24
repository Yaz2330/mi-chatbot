# 🤖 Chatbot Tutor de Marketing Digital

Este proyecto consiste en la creación de un **chatbot académico personalizado** que responde preguntas basadas en el contenido del PDF _“Marketing Digital para Principiantes”_ de FRSKO Academy. Fue desarrollado en **Python** y ejecutado inicialmente en **Google Colab**, con una implementación final compatible con ejecución local mediante el modelo **DeepSeek LLM**.

---

## 🧩 Fases del Proyecto

### 📁 Fase 1: Preparar el contenido
- Se utilizó el PDF: `Marketing_Digital_Para_Principiantes_-_FRSKO_Academy.pdf`.
- El documento tiene 30 páginas con contenido textual ideal para vectorizar.

### 📄 Fase 2: Cargar y segmentar el PDF
- Se extrajo el texto del PDF y se dividió en fragmentos pequeños.
- Los fragmentos se guardaron para análisis semántico.
- Archivo generado: `fragmentos.txt`

### 🧠 Fase 3: Vectorización del contenido
- Se utilizó el modelo `all-mpnet-base-v2` de la librería `sentence-transformers`.
- Se generaron **embeddings** para cada fragmento.
- Archivo generado: `embeddings.npy`

#### Fragmento de código utilizado:

```python
from sentence_transformers import SentenceTransformer
import numpy as np

modelo = SentenceTransformer('all-mpnet-base-v2')
embeddings = modelo.encode(fragmentos, show_progress_bar=True)
np.save("embeddings.npy", embeddings)
🤖 Fase 4: Construcción del chatbot
Subir el repositorio local a GitHub
Asegúrate de que el proyecto esté completo y funcional hasta esta fase.
Configura el repositorio como privado antes de subirlo.

Crear un llamado local al modelo DeepSeek
Implementa el modelo deepseek-llm-7b-chat para que funcione localmente desde un script.
Habilita la interacción vía terminal, donde el usuario ingresa texto y recibe respuestas.

Agregar los archivos vectorizados al flujo
Incorpora los archivos con embeddings al proceso.
Utiliza un mecanismo de búsqueda semántica local (ejemplo: FAISS, numpy) para conectar preguntas con fragmentos relevantes del PDF.

Personalizar el chatbot
Ajusta parámetros como:

temperature para controlar creatividad o precisión

max_tokens para limitar la longitud de la respuesta

Instrucciones iniciales para que el chatbot se comporte como tutor o asistente académico

🧪 Fase 5: Prueba del agente
Interactuar con el chatbot
Realiza al menos tres preguntas relacionadas con el contenido del PDF.
Verifica que las respuestas sean coherentes y relevantes.

Ajuste fino
Modifica parámetros del modelo o del motor de búsqueda en caso de respuestas imprecisas.
Ajusta el número de fragmentos (top_k) y el formato del prompt para mejorar la interacción.

Documentar el proceso
Deja evidencia en el repositorio, incluyendo:

Instrucciones para uso

Dificultades encontradas (memoria, ambigüedad, rendimiento)

Capturas de pantalla de las interacciones finales

⚙️ Requisitos
Instala las dependencias necesarias:

bash
Copiar
Editar
pip install transformers sentence-transformers torch accelerate
Requiere entorno Python 3.8+ y al menos 16 GB de RAM (si usas CPU) o GPU compatible para eficiencia.

🧪 Cómo ejecutar el chatbot
Ejecuta el script de vectorización para generar los embeddings:

bash
Copiar
Editar
python vectorizar_pdf.py
Esto crea:

embeddings.npy

segments.npy

Ejecuta el chatbot localmente desde terminal:

bash
Copiar
Editar
python deepseek_chat.py
Escribe tus preguntas en la consola. Para salir, escribe:

bash
Copiar
Editar
salir
📁 Archivos principales del proyecto
Archivo	Descripción
deepseek_chat.py	Script principal del chatbot
vectorizar_pdf.py	Script para generar embeddings del PDF
embeddings.npy	Representación numérica del contenido
segments.npy	Fragmentos de texto procesados
README.md	Documentación del proyecto
Marketing_Digital_Para_Principiantes_-_FRSKO_Academy.pdf	Documento fuente

📝 Licencia
Proyecto con fines educativos y personales. El modelo LLM fue proporcionado por DeepSeek AI.

✨ Autora
Yaz2330
Proyecto desarrollado como parte de una exploración académica en chatbots personalizados con enfoque en educación digital.

