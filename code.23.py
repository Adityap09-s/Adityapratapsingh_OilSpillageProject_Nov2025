# file: 7_similarity_demo.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Example documents
docs = [
    "I love machine learning and NLP",
    "NLP and machine learning are amazing",
    "Cooking recipes are fun to try",
]

# TF-IDF representation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# Compute cosine similarity
sim_matrix = cosine_similarity(X)

# Pretty print
print("Cosine Similarity Matrix:\n")
df = pd.DataFrame(sim_matrix, index=[f"Doc{i+1}" for i in range(len(docs))],
                  columns=[f"Doc{i+1}" for i in range(len(docs))])
print(df.round(3))
