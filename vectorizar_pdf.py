import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import numpy as np

# Función para extraer texto de un PDF
def extraer_texto_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texto = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        texto += page.get_text()
    return texto

# Extraer texto del PDF
pdf_path = "Marketing_Digital_Para_Principiantes_-_FRSKO_Academy.pdf"  # Ruta de tu PDF
texto_pdf = extraer_texto_pdf(pdf_path)

# Dividir el texto en segmentos
segmentos = texto_pdf.split("\n\n")

# Cargar el modelo de sentence-transformers
model = SentenceTransformer('all-MiniLM-L6-v2')

# Crear los embeddings de cada segmento
embeddings = model.encode(segmentos)

# Guardar los embeddings y segmentos
np.save('embeddings.npy', embeddings)
np.save('segments.npy', segmentos)

print("Embeddings y segmentos guardados exitosamente.")
