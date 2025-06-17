# Aufruf der HuggingFace-Pipeline

from transformers import pipeline
from src.labels import load_label_config, flatten_labels

MODEL_NAME = "facebook/bart-large-mnli"
_classifier = None 

def get_classifier():
    # Lädt das Modell nur einmal und cached es.
    global _classifier
    if _classifier is None:
        print("Lade Modell...")
        _classifier = pipeline("zero-shot-classification", model=MODEL_NAME)
        print("Modell geladen.")
    return _classifier

def classify_prompt(prompt: str) -> dict:
    # Klassifiziert einen Prompt in alle verfügbaren Kategorien.
    label_config = load_label_config()
    classifier = get_classifier()

    result = {}
    for category, labels in label_config.items():
        res = classifier(prompt, candidate_labels=labels)
        result[category] = {
            "label": res["labels"][0],
            "scores": dict(zip(res["labels"], [round(s, 4) for s in res["scores"]]))
        }

    return {
        "prompt": prompt,
        "result": result
    }
