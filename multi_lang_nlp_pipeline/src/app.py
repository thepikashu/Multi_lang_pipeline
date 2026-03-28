import streamlit as st
import pandas as pd
from pipeline import process_full_pipeline

st.set_page_config(page_title="Multilingual NLP Pipeline", layout="wide")

st.title("Advanced Multilingual NLP Pipeline")
st.markdown("Developed by **Yashasvee Taiwade** | IIT Bombay")

user_input = st.text_area("Enter text (French, German, Hindi, English, etc.):", height=150)

if st.button("Run Intelligence Pipeline"):
    if user_input.strip():
        with st.spinner("Analyzing linguistic patterns..."):
            results = process_full_pipeline(user_input)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Translation & Language")
                st.info(f"Detected Language: **{results['source_lang'].upper()}**")
                st.write("**English Translation:**")
                st.write(results['translated'])
                
                st.subheader("Emotion Analysis")
                emo = results['emotion']
                st.metric(label="Detected Emotion", value=emo['label'].upper(), delta=f"{emo['score']:.2%}")

            with col2:
                st.subheader("Named Entity Recognition")
                if isinstance(results['ner'], list) and len(results['ner']) > 0:
                    st.table(pd.DataFrame(results['ner']))
                else:
                    st.write("No major entities found.")

            st.divider()
            st.subheader("Linguistic Features (SpaCy)")
            tab1, tab2 = st.tabs(["Noun Phrases", "Tokens"])
            with tab1:
                # Fixed: Changed 'basic' to 'linguistics'
                st.write(", ".join(results['linguistics']['noun_phrases']))
            with tab2:
                # Fixed: Changed 'lemmas' to 'tokens'
                st.write(", ".join(results['linguistics']['tokens']))
