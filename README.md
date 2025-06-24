# 🤖 Chatbot Tutor de Marketing Digital

Este proyecto consiste en la creación de un **chatbot académico** que responde preguntas basadas en el contenido del PDF _“Marketing Digital para Principiantes”_ de FRSKO Academy. Fue desarrollado en **Python** y ejecutado inicialmente en **Google Colab** por motivos de espacio.

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

## 💻 Interacción y pruebas en Google Colab

La fase de interacción con el chatbot se realizó en un entorno Google Colab para facilitar la ejecución rápida y prueba del modelo y búsqueda semántica.

Puedes acceder al notebook con todo el código, ejecución y pruebas desde este enlace:

[👉 Abrir Notebook en Google Colab](https://colab.research.google.com/drive/1iSwoVfLMbQmACg6DGrdz_tlsTVNjIG75)

---
