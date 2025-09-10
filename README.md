# Data Cleaning & Transformation Pipeline

This repo packages the **notebook-based data cleaning & transformation** into a **reproducible script** and a **batch runner** so you can process many files automatically.

## Project structure
```text
df-cleaning-pipeline/
├─ src/
│  ├─ user_pipeline.py          # your exported notebook logic (names & order preserved)
│  ├─ notebook_with_outputs.py  # same logic with auto-display of last expression
│  └─ pipeline.py               # automation CLI: runs your logic over many files
├─ notebooks/
│  └─ DataFrames.ipynb          # cleaned, Colab-friendly notebook
├─ docs/
│  ├─ verification_report.md
│  ├─ cell_verification_report.csv
│  └─ notebook_notes.md
├─ data/                         # place input files here (optional)
├─ outputs/                      # results are saved here
├─ tests/
│  └─ smoke_test.py
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

## 1) Set up locally
```bash
# (a) Install Git (https://git-scm.com/downloads) if not already installed
# (b) Open a terminal in this folder

# Create a virtual environment (recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2) Run the pipeline (single file)
```bash
python -m src.pipeline --pipeline src/user_pipeline.py         --input data/raw.csv         --output-dir outputs/runs
```

## 3) Run the pipeline (batch over a folder)
```bash
python -m src.pipeline --pipeline src/user_pipeline.py         --input-dir data/raw         --glob "*.csv"         --output-dir outputs/runs
```

> The runner sets `INPUT_FILE`, `OUTPUT_DIR`, and `CURRENT_BASENAME` for your code. It also auto-saves any DataFrames whose variable names match `^(df$|df_.*|clean.*|final.*|.*_clean$|.*_final$)` into the per-file output folder.

## 4) (Optional) Run the notebook
```bash
pip install jupyter ipykernel
jupyter notebook notebooks/DataFrames.ipynb
```

## 5) Create a GitHub repository (from scratch)
1. Go to https://github.com/new and create an **empty** repo (don’t tick README or License).
2. Copy the repo URL (it looks like `https://github.com/<you>/<repo>.git`).

Back in your terminal (in this project folder), run:
```bash
git init
git add .
git commit -m "Initial commit: data cleaning pipeline + automation"
git branch -M main
git remote add origin YOUR_REPO_URL_HERE
git push -u origin main
```

## 6) Typical next commits
- Add sample data to `data/` (if small), or keep it out of Git if large/sensitive.
- Update `requirements.txt` with pinned versions once stable (e.g., `pandas==2.2.2`).
- Add a short usage example and expected outputs in the README.

## 7) Optional: simple test
```bash
python -m pytest -q tests/smoke_test.py
```

---

**Notes**  
- Your original variable and function names are preserved in `src/user_pipeline.py`.
- If your notebook had hardcoded paths, you can switch to reading `INPUT_FILE`:
  ```python
  import os, pandas as pd
  path = os.getenv("INPUT_FILE", "fallback.csv")
  df = pd.read_csv(path)
  ```
- The batch runner saves any DataFrames with "clean/final" naming patterns per file.
