# Prompt Intent Classifier

Ein kleines, modular aufgebautes Projekt, um Prompts mithilfe von Hugging Face Zero-Shot-Modellen (z. B. `facebook/bart-large-mnli`) automatisch nach Intent, Domain oder Schwierigkeitsgrad zu klassifizieren.

## Beispiel
```json
{
  "input": "Wie kann ich meine Steuerlast reduzieren?",
  "output": {
    "intent": "Frage",
    "domain": "Finanzen",
    "difficulty": "medium"
  }
}
```

## Struktur
- `config/labels.yaml`: Definiert Klassifikationslabels
- `src/`: Modellaufruf & Logik
- `scripts/classify_prompt.py`: CLI-Testskript
- `notebooks/`: Interaktive Testumgebung mit Jupyter

## Installation
```bash
pip install transformers torch
```

## Starten (Beispielskript)
```bash
python scripts/classify_prompt.py "Wie kann ich meine Steuerlast reduzieren?"
```
