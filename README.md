# GDP Forecasting Pipeline — ARIMA vs LSTM

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

A production-ready, **reproducible** pipeline for **GDP forecasting** across countries.  
It automates **data cleaning & transformations**, trains **ARIMA** (classical) and **LSTM** (deep learning) models, and evaluates using **RMSE** as the primary metric. The repo ships with a Colab-friendly notebook, a command-line **batch runner** to process many files in one go, and clear setup instructions.

---

## Table of Contents
- [Project Summary](#project-summary)
- [Problem Statement](#problem-statement)
- [Data & Assumptions](#data--assumptions)
- [Tools & Libraries](#tools--libraries)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Automation (Batch Runner)](#automation-batch-runner)
- [Cleaning & Transformation Workflow](#cleaning--transformation-workflow)
- [Modeling Methods](#modeling-methods)
- [Evaluation (RMSE)](#evaluation-rmse)
- [Results](#results)
- [Reproducibility Notes](#reproducibility-notes)
- [Roadmap / Future Work](#roadmap--future-work)
- [License](#license)

---

## Project Summary
This project compares **ARIMA** and **LSTM** for **GDP time-series forecasting** across multiple countries. It includes:

- A **notebook** for exploration and visualization (`notebooks/DataFrames.ipynb`)
- An **exported script** with the exact notebook logic (`src/user_pipeline.py`)
- A **CLI batch runner** to execute the pipeline for many files automatically (`src/pipeline.py`)
- **RMSE-based** evaluation and a tidy results table
- A **reproducible environment** (`requirements.txt`) and clean repo layout

---

## Problem Statement
> Given historical GDP series (by country), build a reproducible pipeline that:
> 1) **Cleans & transforms** data consistently,  
> 2) Trains **ARIMA** and **LSTM** models per country,  
> 3) **Evaluates** using **Root Mean Squared Error (RMSE)**, and  
> 4) **Automates** batch runs across many input files.

Business framing: minimize forecast error to support budgeting, macro planning, and scenario analysis per country.

---

## Data & Assumptions
- **Target:** GDP (level values by period).
- **Granularity:** Country-level time series.
- **Split:** Time-based (train → validation → test).
- **Scale differences:** Countries have different GDP magnitudes; **compare RMSE within a country**, not across countries.
- **Transforms:** Minimal and consistent per series (see workflow below).

> ⚠️ Data files are not committed by default. Place inputs under `data/` or pass a path via CLI.

---

## Tools & Libraries
- **Python** (3.10+), **pandas**, **numpy**
- **statsmodels** for ARIMA
- **TensorFlow/Keras** (or PyTorch) for LSTM
- **Jupyter / Colab** for exploration

(Actual imports are listed in `requirements.txt`.)

---

## Repository Structure
```
gdp-forecasting-pipeline/
├─ src/
│  ├─ user_pipeline.py          # exported notebook logic (names & order preserved)
│  ├─ notebook_with_outputs.py  # same logic with auto-display of last expression
│  └─ pipeline.py               # automation CLI: batch-runs your logic
├─ notebooks/
│  └─ DataFrames.ipynb          # Colab-friendly notebook
├─ data/                        # place input files here (optional)
├─ outputs/                     # predictions/metrics land here
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

---

## Quick Start

```bash
# 1) Create a virtual environment (recommended)
python -m venv .venv
# Windows: .venv\Scriptsctivate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

### (Optional) Run the notebook
```bash
pip install jupyter ipykernel
jupyter notebook notebooks/DataFrames.ipynb
```

---

## Automation (Batch Runner)

**Single file**
```bash
python -m src.pipeline --pipeline src/user_pipeline.py   --input data/raw.csv   --output-dir outputs/runs
```

**Folder batch**
```bash
python -m src.pipeline --pipeline src/user_pipeline.py   --input-dir data/raw   --glob "*.csv"   --output-dir outputs/runs
```

The runner injects:
- `INPUT_FILE` → current file path  
- `OUTPUT_DIR` → per-file output folder  
- `CURRENT_BASENAME` → filename stem  

After execution, it **auto-saves** any pandas **DataFrame** globals whose names match:

```
^(df$|df_.*|clean.*|final.*|.*_clean$|.*_final$)
```

---

## Cleaning & Transformation Workflow
1. **Load**: Read CSV/Excel; enforce dtypes for date/time & numeric columns.  
2. **Standardize schema**: Normalize column names (e.g., `Country`, `date`, `gdp`); trim whitespace; fix country casing.  
3. **Data quality**: Handle missing values (forward-fill short gaps; drop leading/trailing null blocks); drop duplicates; ensure strictly increasing dates per country.  
4. **Outlier sanity checks**: Flag extreme jumps; conservative winsorization only if clearly erroneous.  
5. **Model shaping**:  
   - **ARIMA**: allow differencing (`d`) via model selection; univariate target.  
   - **LSTM**: create supervised sequences with a lookback window (e.g., 12/16/24), train/val/test split, fit scaler on train only, inverse-transform predictions before scoring.  
6. **Save artifacts**: Final/cleaned DataFrames saved under `outputs/` by the runner when variables are named like `df_*`, `*_clean`, `*_final`.

---

## Modeling Methods

### ARIMA (AutoRegressive Integrated Moving Average)
- Fit per country; select `(p,d,q)` via info criteria (AIC) or a small grid.
- Seasonal terms typically off for GDP unless strictly seasonal.
- Forecast the test horizon; evaluate with RMSE.

**Why ARIMA?** Strong baseline for univariate series; trend/difference handled cleanly; fast & interpretable.

### LSTM (Long Short-Term Memory)
- Univariate sequence on normalized GDP values.
- Architecture: 1–2 LSTM layers (32–64 units) → Dense; dropout as needed.
- Early stopping on validation to prevent overfitting.
- Predictions inverse-transformed to original units before RMSE.

**Why LSTM?** Captures non-linearities and long dependencies; useful counterpoint to classical models.

---

## Evaluation (RMSE)
We use **Root Mean Squared Error (RMSE)** as the **primary metric**.

- RMSE is in **original units** (GDP), so large economies → large RMSE; that’s expected.  
- **Lower RMSE is better**.  
- Compare **within the same country** (same scale).  
- “Accuracy (%)” can be reported for intuition, but **RMSE drives selection**.

---

## Results

**Winner per country (by RMSE)**  
- **China:** **ARIMA** better  
- **Japan:** **ARIMA** better  
- **UK:** **ARIMA** better  
- **USA:** **LSTM** better

**Comparison table (rounded):**

| Country | LSTM RMSE | LSTM Accuracy (%) | ARIMA RMSE | ARIMA Accuracy (%) |
|:--|--:|--:|--:|--:|
| China | 3,255,896 | 80.64 | **2,242,993** | **86.66** |
| Japan | 745,692   | 84.38 | **588,398**   | **87.68** |
| UK    | 499,067   | 83.26 | **242,067**   | **91.88** |
| USA   | **1,944,027** | **91.75** | 3,538,478 | 84.98 |

> Takeaway: ARIMA wins in three countries; LSTM wins in the USA → use **per-country** model selection.

---

## Reproducibility Notes
- **Notebook → Script parity:** `src/user_pipeline.py` is exported from the notebook; variable/function names and execution order are preserved.  
- **Colab-friendly:** `notebooks/DataFrames.ipynb` uses valid nbformat fields.  
- **Determinism:** For LSTM, set seeds if strict reproducibility is required (GPU/parallelism may still introduce variance).

---

## Roadmap / Future Work
- Add NRMSE/sMAPE/MASE alongside RMSE for scale-free reporting.  
- Handle structural breaks / calendar effects.  
- Add multivariate signals (CPI, PMI, exports) and ML baselines (XGBoost/VAR/Prophet).  
- Hyperparameter search with time-series cross-validation.  
- Model registry to store best per-country artifacts.  
- CI (GitHub Actions) to run tests on push.

---

## License
Released under the **MIT License**. See `LICENSE`.
