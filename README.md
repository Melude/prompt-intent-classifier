# Prompt Intent Classifier

Ein kleines, modular aufgebautes Projekt, um Prompts mithilfe von Hugging Face Zero-Shot-Modellen (z. B. `facebook/bart-large-mnli`) automatisch nach Intent, Domain oder Schwierigkeitsgrad zu klassifizieren.

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

- `config/labels.yaml`: Definiert die verfügbaren Klassifikationslabels
- `data/example_prompts.txt`: Beispiel-Prompts zur Analyse
- `src/`: Modelllogik und Utilities
  - `classifier.py`: Modell-Wrapper und Klassifikation
  - `labels.py`: Einlesen und Verarbeiten der Labels
  - `utils/`: Hilfsfunktionen 
- `scripts/classify_prompt.py`: CLI-Testskript
- `notebooks/`: Interaktive Analyse und Evaluation mit Jupyter

## Installation

```bash
pip install -r requirements.txt
```

## Starten (Beispielskript)

```bash
python scripts/classify_prompt.py "Wie kann ich meine Steuerlast reduzieren?"
```
## Hinweis

Dieses Projekt eignet sich ideal, um Promptdaten in Klassifikationspipelines einzubinden.