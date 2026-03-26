# © 2026 Yashasvee Taiwade - Research/Portfolio Use
from transformers import pipeline
import spacy
import streamlit as st

# Load SpaCy for faster, more accurate basic NLP
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

@st.cache_resource
def get_pipelines():
    """
    Cache models so they only load once.
    """
    ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)
    # Using a specialized emotion model
    emotion = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
    return ner, emotion

ner_pipe, emotion_pipe = get_pipelines()

def advanced_ner(text):
    try:
        entities = ner_pipe(text)
        return [{"entity": ent['entity_group'], "word": ent['word'], "score": round(float(ent['score']), 4)} for ent in entities]
    except Exception as e:
        return f"NER Error: {e}"

def analyze_emotion(text):
    """Detects Joy, Anger, Fear, Sadness, etc."""
    try:
        results = emotion_pipe(text)
        return results[0] # Returns {'label': 'joy', 'score': 0.99}
    except Exception as e:
        return {"label": "Error", "score": 0.0}

def spacy_processor(text):
    """Replacement for TextBlob using SpaCy logic"""
    doc = nlp(text)
    return {
        "tokens": [token.text for token in doc],
        "noun_phrases": [chunk.text for chunk in doc.noun_chunks],
        "lemmas": [token.lemma_ for token in doc if not token.is_stop]
    }
