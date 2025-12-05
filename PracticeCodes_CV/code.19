# file: 3_tune_grid.py

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Tiny demo dataset
texts = [
    "excellent movie with great acting",
    "terrible plot and awful pacing",
    "loved every moment, fantastic!",
    "boring and predictable",
    "superb cinematography and direction",
    "weak script and bad acting",
    "what a masterpiece",
    "not good at all",
    "brilliant experience overall",
    "do not recommend"
]

y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])  # 1=positive, 0=negative

# Step 1: Build pipeline
pipe = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Step 2: Define grid of hyperparameters
param_grid = {
    "tfidf__ngram_range": [(1, 1), (1, 2)],
    "tfidf__min_df": [1, 2],
    "tfidf__analyzer": ["word", "char_wb"],
    "clf__C": [0.25, 1.0, 4.0]  # regularization strength
}

# Step 3: Run Grid Search with 3-fold cross-validation
search = GridSearchCV(pipe, param_grid, cv=3, n_jobs=-1, scoring="f1")
search.fit(texts, y)

# Step 4: Print results
print("Best parameters found:")
print(search.best_params_)
print("\nBest cross-validation F1 score:", search.best_score_)

# Step 5: Test the best model on a sample
best_model = search.best_estimator_
sample_text = ["not a great movie but had moments"]
print("\nSample prediction:", best_model.predict(sample_text))
