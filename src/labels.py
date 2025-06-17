# Laden & Struktur der Labels

import yaml
import os

def load_label_config():
    # Lädt die Labels aus labels.yaml als Dictionary (intent, domain, difficulty).
    path = os.path.join(os.path.dirname(__file__), "..", "config", "labels.yaml")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def flatten_labels(label_config: dict) -> list:
    # Gibt eine flache Liste aller Label-Werte zurück (für zero-shot pipeline).
    all_labels = []
    for category_labels in label_config.values():
        all_labels.extend(category_labels)
    return all_labels
