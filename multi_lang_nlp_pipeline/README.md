# 🌐 Multi-Language NLP Pipeline

This project is a multi-language Natural Language Processing (NLP) pipeline that:
- Detects the input language,
- Translates it to English (if needed),
- Performs basic NLP analysis,
- Extracts named entities using advanced NER,
- Evaluates sentiment with a modern transformer-based model.

Built with `Streamlit`, it's designed to be both interactive and beginner-friendly.

---

## 🚀 Demo

Launch the app locally with:

```bash
streamlit run src/app.py
```
---
## 📦 Features
- 🧠 Language Detection & Translation: Auto-detects language and translates to English using deep_translator.

- 🗣️ Basic NLP Analysis: Tokenization, polarity, subjectivity, and noun phrase extraction.

- 🔍 Advanced NER: Named Entity Recognition powered by transformer models (e.g., spaCy or HuggingFace).

- ❤️ Advanced Sentiment Analysis: High-quality sentiment classification beyond simple polarity.

- 🌐 Multilingual Support: Accepts input in most languages (tested with English, French, German, Spanish, etc).

- 🧪 Streamlit UI: Intuitive and responsive web UI for testing and demos.

---
## 📁 Project Structure

your-project/
│
├── src/
│   ├── app.py              # Streamlit frontend
│   ├── pipeline.py         # NLP pipeline logic
│   ├── nlp_processor.py    # Basic NLP functions
│   ├── advanced_nlp.py     # Advanced NER and sentiment
│
├── data/
│   ├── english_sample.txt         # Demo input in English
│   ├── french_sample.txt      # French example
│   └── ...                 # Add more multilingual samples here
│
├
│
├── requirements.txt
└── README.md


---

## 📝 Sample Input Texts

You can test the app with pre-written multilingual samples in the data/ folder. For example:

" Sport and Fitness in Your 30s:
Staying active in your 30s is essential for maintaining overall health and well-being..."

Add your own .txt files in different languages to extend the demo.


---
## 🔧 Installation

- Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

- Install dependencies:

```bash
pip install -r requirements.txt

```

- Then run the app:

```bash
streamlit run src/app.py

```

---

## 🔍 Requirements
Key packages:

- streamlit

- langdetect

- deep_translator

- spacy

- transformers

- textblob (or similar for basic NLP)

- pandas (for tabular display of NER)

---

## 📄 License

MIT License

---

## 👩‍💻 Author
[M26I](https://github.com/M26I)

---
© 2025 M26I – For educational/portfolio use only.  
Unauthorized use or redistribution without credit is prohibited.