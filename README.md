# Multi-Language NLP Pipeline

## Overview

This project is an end-to-end multilingual NLP pipeline that processes user input across different languages and performs translation, linguistic analysis, named entity recognition (NER), and sentiment analysis.
The pipeline is deployed using Streamlit for an interactive web interface.


## My Contributions

* Moved beyond basic lexicons to implement a deep-learning inference engine using BERT-Large (NER) and DistilBERT (Emotion Classification).
* Integrated deep-translator with langdetect to create a seamless translation-to-analysis workflow for non-English inputs (Hindi, German, French).
* Swapped TextBlob for SpaCy to provide production-standard tokenization and noun-phrase extraction.
* Optimized model loading with Streamlit caching and configured the backend for CUDA-accelerated GPU inference (Torch-based).
* Created a synthetic multilingual dataset (benchmark_tests.json) and generated a performance report to verify model confidence across languages.


## Features

* **Language Detection & Translation**
  Automatically detects input language and translates to English

* **Basic NLP Analysis**
  Tokenization, noun phrases, polarity, subjectivity

* **Named Entity Recognition (NER)**
  Extracts entities using transformer-based models

* **Sentiment Analysis**
  Context-aware sentiment classification

* **Streamlit UI**
  Simple interface for real-time interaction


## Sample Inputs

You can test with multilingual text such as:

* English
* French
* German
* Spanish

Or add your own `.txt` files in the `data/` folder.

## Results

The pipeline was evaluated using the provided notebook/ against multilingual test cases.  
* NER Confidence: Achieved high precision in identifying entities like "IIT Bombay" and "Paris" within translated contexts.
* Emotion Granularity: Successfully mapped inputs to specific states (Joy, Anger, Love) with confidence scores typically $> 90\%$.
![Emotion Distribution Chart](results/emotion_chart.png)

## Key Learnings

* Combining multiple NLP tasks into a pipeline improves usability
* Translation quality affects downstream NLP performance
* Transformer models significantly improve NER and sentiment accuracy
* Handling multilingual inputs introduces preprocessing challenges


## Author

Yashasvee Taiwade
