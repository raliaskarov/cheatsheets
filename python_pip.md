# Commands for package management in python


## Check if packages are installed
```
import importlib

packages = [
    "transformers",
    "datasets",
    "sentencepiece",
    "accelerate",
    "evaluate",
    "rouge_score",
    "bert_score",
    "sentence_transformers",
    "spacy",
]

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"✅ {pkg} is installed")
    except ImportError:
        print(f"❌ {pkg} is NOT installed")

]
```
