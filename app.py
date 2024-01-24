from flask import Flask, request, jsonify
from Levenshtein import distance as levenshtein_distance
from transformers import AutoTokenizer, AutoModel
import numpy as np
import spacy
from scipy.spatial.distance import cosine
import torch
import spacy.cli


# Initializing Flask app
app = Flask(__name__)

# Loading models and tokenizers for sentiment_similarity
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')


# downloading and loading spacy data for embedding_similarity
spacy.cli.download("en_core_web_lg")
spacy.cli.download("en_core_web_md")

nlp = spacy.load("en_core_web_md")  # Make sure to download this model first


# Character-wise similarity
def char_similarity(text1, text2):
    max_len = max(len(text1), len(text2))
    if max_len == 0:  # Avoid division by zero
        return 1.0
    return 1 - levenshtein_distance(text1, text2) / max_len

# Simple word overlap similarity
def simple_word_similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    common_words = words1.intersection(words2)
    total_words = words1.union(words2)
    if not total_words:
        return 1.0  # Avoid division by zero if both texts are empty
    return len(common_words) / len(total_words)


# sentiment-wise similarity
def sentiment_similarity(text1, text2):
    # Tokenize and encode the texts
    text1_tokens = tokenizer(text1, return_tensors='pt', padding=True, truncation=True)
    text2_tokens = tokenizer(text2, return_tensors='pt', padding=True, truncation=True)
    
    # Get embeddings
    with torch.no_grad():
        text1_embedding = model(**text1_tokens).last_hidden_state.mean(dim=1).squeeze(0)
        text2_embedding = model(**text2_tokens).last_hidden_state.mean(dim=1).squeeze(0)
    
    # Calculating cosine similarity and adjusting the range to [0, 1]
    cosine_sim = 1 - cosine(text1_embedding, text2_embedding)  
    normalized_sim = (cosine_sim + 1) / 2  # normalizing the value range 0 to 1
    return normalized_sim

# Embedding-based word similarity using SpaCy
def embedding_similarity(text1, text2, nlp):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)

# endpoints
@app.route('/char_similarity', methods=['POST'])
def character_similarity():
    data = request.json
    score = char_similarity(data['text1'], data['text2'])
    return jsonify({"similarity score": score})

@app.route('/word_similarity', methods=['POST'])
def word_similarity():
    data = request.json
    score = simple_word_similarity(data['text1'], data['text2'])
    return jsonify({"similarity score": score})

@app.route('/sentiment_similarity', methods=['POST'])
def sentiment_sim():
    data = request.json
    score = sentiment_similarity(data['text1'], data['text2'])
    return jsonify({"similarity score": score})

@app.route('/embedding_similarity', methods=['POST'])
def embedding_sim():
    data = request.json
    score = embedding_similarity(data['text1'], data['text2'], nlp)
    return jsonify({"similarity score": score})

@app.route('/all_similarities', methods=['POST'])
def all_similarities():
    data = request.json
    char_sim = char_similarity(data['text1'], data['text2'])
    word_sim = simple_word_similarity(data['text1'], data['text2'])
    embed_sim = embedding_similarity(data['text1'], data['text2'], nlp)
    sent_sim = sentiment_similarity(data['text1'], data['text2'])
    return jsonify({
        "Character-wise similarity": char_sim,
        "Word overlap similarity": word_sim,
        "Embedding-based word similarity": embed_sim,
        "Sentiment-wise similarity": sent_sim
    })

if __name__ == '__main__':
    app.run(debug=True)


http://127.0.0.1:5000/char_similarity

http://127.0.0.1:5000/word_similarity


http://127.0.0.1:5000/sentiment_similarity


http://127.0.0.1:5000/embedding_similarity


http://127.0.0.1:5000/all_similarities
