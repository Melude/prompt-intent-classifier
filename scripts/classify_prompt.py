# CLI-Skript für einfache Tests

import sys
import os
from src.classifier import classify_prompt

def main():
    if len(sys.argv) < 2:
        print("Bitte gib einen Prompt als Argument an.")
        print("Beispiel:")
        print("  python3 scripts/classify_prompt.py \"Wie kann ich meine Steuerlast reduzieren?\"")
        sys.exit(1)

    prompt = sys.argv[1]
    result = classify_prompt(prompt)

    print("\nKlassifikationsergebnis:")
    print(f"- Prompt: {result['prompt']}")
    for category, data in result["result"].items():
        label = data["label"]
        score = data["scores"].get(label, 0.0)
        print(f"- {category.capitalize()}: {label}  (Top Score: {round(score, 3)})")

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    main()
