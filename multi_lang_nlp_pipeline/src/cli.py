# © 2026 Yashasvee Taiwade | CLI Tool
import argparse
from pipeline import process_full_pipeline

def main():
    parser = argparse.ArgumentParser(description="Advanced Multi-language NLP CLI")
    parser.add_argument("-t", "--text", type=str, help="Text to process")
    parser.add_argument("-o", "--output", type=str, help="Output file (CSV)")
    
    args = parser.parse_args()
    user_text = args.text if args.text else input("Enter text for analysis: ")
    
    print("\n--- Running Transformer Inference ---")
    results = process_full_pipeline(user_text)
    
    print(f"\n[Detected Lang]: {results['source_lang'].upper()}")
    print(f"[Translation]: {results['translated']}")
    print(f"[Emotion]: {results['emotion']['label']} ({results['emotion']['score']})")
    print(f"[Entities]: {', '.join([e['word'] for e in results['ner']])}")

if __name__ == "__main__":
    main()
