
from transformers import pipeline
import spacy
import torch

# Load SpaCy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm -q")
    nlp = spacy.load("en_core_web_sm")

# Detect Hardware
device = 0 if torch.cuda.is_available() else -1

# FIX: Changed 'grouped_entities' to 'aggregation_strategy'
ner_pipe = pipeline(
    "ner", 
    model="dbmdz/bert-large-cased-finetuned-conll03-english", 
    aggregation_strategy="simple", 
    device=device
)

emotion_pipe = pipeline(
    "text-classification", 
    model="bhadresh-savani/distilbert-base-uncased-emotion", 
    device=device
)

def advanced_ner(text):
    entities = ner_pipe(text)
    # The output format changes slightly with aggregation_strategy
    return [{"word": ent['word'], "entity": ent['entity_group'], "score": round(float(ent['score']), 3)} for ent in entities]

def analyze_emotion(text):
    res = emotion_pipe(text)[0]
    return {"label": res['label'], "score": round(float(res['score']), 3)}

def spacy_processor(text):
    doc = nlp(text)
    return {
        "tokens": [t.text for t in doc[:10]],
        "noun_phrases": [c.text for c in doc.noun_chunks]
    }
