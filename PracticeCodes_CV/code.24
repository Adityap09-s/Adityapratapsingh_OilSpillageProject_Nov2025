# file: 8_topic_modeling.py
from gensim import corpora, models

# Example dataset
docs = [
    "I love deep learning and natural language processing",
    "Artificial intelligence is the future",
    "Cooking and baking are my hobbies",
    "I enjoy trying new recipes in the kitchen",
    "Machine learning and AI are closely related"
]

# Step 1: Tokenize (simple lowercase split)
texts = [doc.lower().split() for doc in docs]

# Step 2: Create dictionary and bag-of-words corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Step 3: Train LDA model (2 topics)
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=10)

# Step 4: Display discovered topics
print("\nDiscovered Topics:\n")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx + 1}: {topic}")
