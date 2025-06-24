# 🤖 Chatbot Tutor de Marketing Digital

Este proyecto consiste en la creación de un **chatbot académico** que responde preguntas basadas en el contenido del PDF **“Marketing Digital para Principiantes”** de FRSKO Academy. Fue desarrollado usando Python y ejecutado en Google Colab por motivos de espacio.

---

## 🧩 Fases del proyecto

### 📁 Fase 1: Preparar el contenido
- Se utilizó el PDF: `Marketing_Digital_Para_Principiantes_-_FRSKO_Academy.pdf`.
- El documento tiene 30 páginas, con contenido textual ideal para vectorizar.

### 📄 Fase 2: Cargar y segmentar el PDF
- Se extrajo el texto del PDF y se dividió en fragmentos para análisis semántico.
- Fragmentos guardados en `fragmentos.txt`.

### 🧠 Fase 3: Vectorización del contenido
- Se utilizó el modelo **all-mpnet-base-v2** de `sentence-transformers`.
- Se crearon los embeddings de cada fragmento.
- Guardado en `embeddings.npy`.

```python
from sentence_transformers import SentenceTransformer
import numpy as np

modelo = SentenceTransformer('all-mpnet-base-v2')
embeddings = modelo.encode(fragmentos, show_progress_bar=True)
np.save("embeddings.npy", embeddings)
