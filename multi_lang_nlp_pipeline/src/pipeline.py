
from langdetect import detect
from deep_translator import GoogleTranslator
from advanced_nlp import advanced_ner, analyze_emotion, spacy_processor

def process_full_pipeline(text):
    try:
        lang = detect(text)
    except:
        lang = "en"
        
    # Translate to English if needed
    translated = GoogleTranslator(source='auto', target='en').translate(text) if lang != 'en' else text
    
    return {
        "original": text,
        "source_lang": lang,
        "translated": translated,
        "ner": advanced_ner(translated),
        "emotion": analyze_emotion(translated),
        "linguistics": spacy_processor(translated)
    }
