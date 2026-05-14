import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Cargar dataset
df = pd.read_csv("dataset.csv")

# Crear pipeline IA
modelo = Pipeline([
    ("vectorizador", TfidfVectorizer()),
    ("clasificador", MultinomialNB())
])

# Entrenar modelo
modelo.fit(df["descripcion"], df["categoria"])

# Función para predecir categoría
def predecir_categoria(texto):

    categoria = modelo.predict([texto])[0]

    probabilidad = modelo.predict_proba([texto])[0]

    confianza = max(probabilidad) * 100

    return categoria, confianza