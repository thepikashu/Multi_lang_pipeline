# © 2026 Yashasvee Taiwade - Research/Portfolio Use
from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator
from advanced_nlp import advanced_ner, analyze_emotion, spacy_processor

DetectorFactory.seed = 0

def process_full_pipeline(text):
    # 1. Detect Language
    lang = detect(text)
    
    # 2. Translate if not English
    if lang != 'en':
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    else:
        translated_text = text
    
    # 3. Run all analyses
    basic = spacy_processor(translated_text)
    ner = advanced_ner(translated_text)
    emotion = analyze_emotion(translated_text)
    
    return {
        "source_lang": lang,
        "translated": translated_text,
        "basic": basic,
        "ner": ner,
        "emotion": emotion
    }
