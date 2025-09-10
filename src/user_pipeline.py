"""
user_pipeline.py — Clean, reproducible data-prep for GDP forecasting
--------------------------------------------------------------------
- No notebook cell markers
- No inline prints/auto_show
- Parameterized file paths
- Produces global DataFrames: merged_df, df_USA, df_UK, df_Japan, df_China
- Keeps variable names simple so the CLI runner can auto-save them

Usage (run by the batch runner):
    python -m src.pipeline --pipeline src/user_pipeline.py --input-dir data/raw --glob "*.csv" --output-dir outputs/runs
Note: This script does not depend on --input/--input-dir; it reads the Excel data listed below.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd


# ---------------------------
# Configuration
# ---------------------------

# Root directory for input Excel files (change if needed)
DATA_DIR = Path(os.getenv("DATA_DIR", "data")).resolve()

# Countries of interest (match exact column names in source files)
COUNTRIES = ["United States", "United Kingdom", "Japan", "China"]

# Year window to keep (inclusive strings for mixed string/int year indices)
YEAR_START = "1994"
YEAR_END   = "2022"


# ---------------------------
# Utilities
# ---------------------------

def _ensure_year_index(df: pd.DataFrame, col: str = "Year") -> pd.DataFrame:
    if col in df.columns:
        df = df.copy()
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
        df = df.set_index(col)
    # ensure Int index if possible
    try:
        df.index = pd.to_numeric(df.index, errors="coerce").astype("Int64")
    except Exception:
        pass
    return df


def _trend_fill_by_index(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """Fill NaNs in each column using a simple line between first and last valid index values (like your notebook)."""
    df = df.copy()
    # ensure Int index for arithmetic
    if not pd.api.types.is_integer_dtype(df.index):
        try:
            df.index = pd.to_numeric(df.index, errors="coerce").astype("Int64")
        except Exception:
            return df

    for c in cols:
        s = df[c]
        first_idx = s.first_valid_index()
        last_idx = s.last_valid_index()
        if first_idx is None or last_idx is None or first_idx == last_idx:
            continue
        slope = (s.loc[last_idx] - s.loc[first_idx]) / (int(last_idx) - int(first_idx))
        missing = s.index[s.isna()]
        if len(missing):
            df.loc[missing, c] = s.loc[first_idx] + slope * (missing.astype(int) - int(first_idx))
    return df


def _select_countries(df: pd.DataFrame, cols: List[str] = None) -> pd.DataFrame:
    cols = cols or COUNTRIES
    keep = [c for c in cols if c in df.columns]
    return df[keep].copy()


def _safe_read_excel(path: Path, **kwargs) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")
    return pd.read_excel(path, **kwargs)


# ---------------------------
# Loaders matching your notebook logic
# ---------------------------

def load_core_cpi() -> pd.DataFrame:
    # Core CPI, seas. adj..xlsx
    df = _safe_read_excel(DATA_DIR / "Core CPI, seas. adj..xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year"] + COUNTRIES]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    df = _trend_fill_by_index(df, ["China"])  # as in your notebook
    return df.rename(columns={
        "United States":"CPI_USA",
        "United Kingdom":"CPI_UK",
        "Japan":"CPI_JAPAN",
        "China":"CPI_CHINA",
    })


def load_imports_merch() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Imports Merchandise, Customs, current US$, millions, seas. adj..xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year"] + COUNTRIES]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    return df.rename(columns={
        "United States":"Imports_USA",
        "United Kingdom":"Imports_UK",
        "Japan":"Imports_JAPAN",
        "China":"Imports_CHINA",
    })


def load_exports_merch() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Exports Merchandise, Customs, current US$, millions, seas. adj..xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year"] + COUNTRIES]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    return df.rename(columns={
        "United States":"Exports_USA",
        "United Kingdom":"Exports_UK",
        "Japan":"Exports_JAPAN",
        "China":"Exports_CHINA",
    })


def load_health_expenditure() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Health Expenditure Final.xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = _ensure_year_index(df)
    df = _trend_fill_by_index(df, ["China"])
    return df.rename(columns={
        "United States":"Health_USA",
        "United Kingdom":"Health_UK",
        "Japan":"Health_JAPAN",
        "China":"Health_CHINA",
    })


def load_unemployment() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Unemployment Rate, seas. adj..xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year", "United States", "United Kingdom", "Japan", "Hong Kong SAR, China"]]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    df = df.rename(columns={"Hong Kong SAR, China": "China"})
    return df.rename(columns={
        "United States":"UNEMP_USA",
        "United Kingdom":"UNEMP_UK",
        "Japan":"UNEMP_JAPAN",
        "China":"UNEMP_CHINA",
    })


def load_gdp() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "GDP at market prices, current US$, millions, seas. adj..xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year"] + COUNTRIES]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    return df.rename(columns={
        "United States":"GDP_USA",
        "United Kingdom":"GDP_UK",
        "Japan":"GDP_JAPAN",
        "China":"GDP_CHINA",
    })


def load_worldbank_indicator(filename: str, value_cols_drop: List[str] = None) -> pd.DataFrame:
    """World Bank-style wide files; drop metadata cols, index by 'Country Name', transpose."""
    df = _safe_read_excel(DATA_DIR / filename)
    # drop metadata columns if present
    value_cols_drop = value_cols_drop or ["Country Code", "Indicator Name", "Indicator Code"]
    for c in value_cols_drop:
        if c in df.columns:
            df.drop(columns=c, inplace=True)
    if "Country Name" in df.columns:
        df.set_index("Country Name", inplace=True)
    df = df.T
    df.index.name = "Year"
    df.columns.name = None
    df = _select_countries(df, COUNTRIES)
    df = df.loc[str(YEAR_START):str(YEAR_END)]
    # fill linear trend per column where missing
    df = _trend_fill_by_index(df, COUNTRIES)
    # cast to float
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def load_manufacturing_pct_gdp() -> pd.DataFrame:
    df = load_worldbank_indicator("Manufacturing Data (% of GDP).xls")
    return df.rename(columns={
        "United States":"Manufacturing_USA",
        "United Kingdom":"Manufacturing_UK",
        "Japan":"Manufacturing_JAPAN",
        "China":"Manufacturing_CHINA",
    })


def load_wgi_sheet(sheet_name: str, rename_prefix: str) -> pd.DataFrame:
    """WGI sheets (Political Stability/Reg Quality/Control of Corr/Gov Effectiveness)."""
    path = DATA_DIR / "wgidataset Final.xlsx"
    df = _safe_read_excel(path, sheet_name=sheet_name)
    df = df.rename(columns={"Unnamed: 0": "Country"})
    df.set_index("Country", inplace=True)
    df_t = df.T
    df_t.index.name = "Year"
    df_t.columns.name = None

    # Insert explicitly missing columns (as in notebook)
    for y in ["1997", "1999", "2001"]:
        if y not in df_t.columns:
            df_t.insert(loc=min(len(df_t.columns), 1), column=y, value=np.nan)  # near start

    # Add 1994/1995 empty then sort
    missing = pd.DataFrame(index=df.index, columns=["1994", "1995"])
    df_new = pd.concat([missing.T, df_t.T], axis=0).sort_index()
    df_out = df_new.T  # back to Year rows, Country cols
    df_out.index.name = "Year"

    keep = _select_countries(df_out, COUNTRIES)
    keep.index = pd.to_numeric(keep.index, errors="coerce").astype("Int64")
    keep = keep.loc[int(YEAR_START):int(YEAR_END)]

    keep = _trend_fill_by_index(keep, COUNTRIES)

    # cast to float
    for c in keep.columns:
        keep[c] = pd.to_numeric(keep[c], errors="coerce")

    return keep.rename(columns={
        "United States": f"{rename_prefix}_USA",
        "United Kingdom": f"{rename_prefix}_UK",
        "Japan": f"{rename_prefix}_JAPAN",
        "China": f"{rename_prefix}_CHINA",
    })


def load_fdi_net_inflows() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "FDI Net Inflows.xlsx")
    if "CountryName" in df.columns:
        df.set_index("CountryName", inplace=True)
    df_t = df.T
    df_t.index.name = "Year"
    df_t.columns.name = None
    df_t = _select_countries(df_t, COUNTRIES)
    df_t.index = pd.to_numeric(df_t.index, errors="coerce").astype("Int64")
    df_t = df_t.loc[int(YEAR_START):int(YEAR_END)]
    return df_t.rename(columns={
        "United States":"FDI_USA",
        "United Kingdom":"FDI_UK",
        "Japan":"FDI_JAPAN",
        "China":"FDI_CHINA",
    })


def load_gov_consumption() -> pd.DataFrame:
    df = load_worldbank_indicator("General government final consumption expenditure (current US$).xls")
    return df.rename(columns={
        "United States":"GovtExp_USA",
        "United Kingdom":"GovtExp_UK",
        "Japan":"GovtExp_JAPAN",
        "China":"GovtExp_CHINA",
    })


def load_exchange_rate() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Exchange rate, new LCU per USD extended backward, period average.xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = df[["Year"] + COUNTRIES]
    df = df.drop([0, df.index[-1]])
    df = _ensure_year_index(df)
    return df.rename(columns={
        "United States":"ExchRate_USA",
        "United Kingdom":"ExchRate_UK",
        "Japan":"ExchRate_JAPAN",
        "China":"ExchRate_CHINA",
    })


def load_life_expectancy() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Life Expectancy at Birth.xlsx")
    df = df.rename(columns={"Unnamed: 0": "Year"})
    df = _ensure_year_index(df)
    # Fill for some countries as in notebook
    df = _trend_fill_by_index(df, ["Japan", "United Kingdom", "United States"])
    return df.rename(columns={
        "United States":"LifeExp_USA",
        "United Kingdom":"LifeExp_UK",
        "Japan":"LifeExp_JAPAN",
        "China":"LifeExp_CHINA",
    })


def load_tourism_arrivals() -> pd.DataFrame:
    df = _safe_read_excel(DATA_DIR / "Tourism Data.xlsx", sheet_name="Tourist Arrivals")
    df = df.rename(columns={"Unnamed: 0": "Country"})
    df.set_index("Country", inplace=True)
    df_t = df.T
    df_t.index.name = "Year"
    # replace '..' with NaN for US
    if "United States" in df_t.columns:
        df_t["United States"] = df_t["United States"].replace("..", np.nan)
    df_t = _trend_fill_by_index(df_t, COUNTRIES)
    for c in COUNTRIES:
        df_t[c] = pd.to_numeric(df_t[c], errors="coerce")
    return df_t.rename(columns={
        "United States":"Tourism_USA",
        "United Kingdom":"Tourism_UK",
        "Japan":"Tourism_JAPAN",
        "China":"Tourism_CHINA",
    })


# ---------------------------
# Build merged dataset (as in notebook)
# ---------------------------

def build_merged() -> pd.DataFrame:
    parts = [
        load_core_cpi(),
        load_imports_merch(),
        load_exports_merch(),
        load_health_expenditure(),
        load_unemployment(),
        load_gdp(),
        load_manufacturing_pct_gdp(),
        load_wgi_sheet("Political StabilityNoViolence", "ViolenceRate"),
        load_fdi_net_inflows(),
        load_gov_consumption(),
        load_exchange_rate(),
        load_wgi_sheet("RegulatoryQuality", "RegQuality"),
        load_wgi_sheet("ControlofCorruption", "Corruption"),
        load_wgi_sheet("GovernmentEffectiveness", "GovtEff"),
        load_life_expectancy(),
        load_tourism_arrivals(),
        load_wgi_sheet("VoiceandAccountability", "VoiceAcc"),
    ]
    # Concatenate by columns on the Year index
    merged = pd.concat(parts, axis=1)
    # Restrict to year window and sort
    try:
        merged.index = pd.to_numeric(merged.index, errors="coerce").astype("Int64")
        merged = merged.loc[int(YEAR_START):int(YEAR_END)]
    except Exception:
        pass
    return merged


def _trade_balance(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    df = df.copy()
    imp = f"Imports_{prefix}"
    exp = f"Exports_{prefix}"
    tb  = f"Trade_Balance_{prefix}"
    if imp in df.columns and exp in df.columns:
        df[tb] = df[exp] - df[imp]
        df.drop(columns=[imp, exp], inplace=True, errors="ignore")
    return df


def _drop_unwanted(df: pd.DataFrame, drop_cols: List[str]) -> pd.DataFrame:
    return df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")


def _move_gdp_last(df: pd.DataFrame, gdp_col: str) -> pd.DataFrame:
    df = df.copy()
    if gdp_col in df.columns:
        g = df.pop(gdp_col)
        df[gdp_col] = g
    return df


def split_by_country(merged: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    out = {}

    # USA
    usa_cols = [c for c in merged.columns if c.endswith("_USA")]
    df_USA = merged[usa_cols].copy()
    df_USA = _drop_unwanted(df_USA, ["CPI_USA", "ExchRate_USA"])
    df_USA = _trade_balance(df_USA, "USA")
    df_USA = _move_gdp_last(df_USA, "GDP_USA")
    out["df_USA"] = df_USA

    # UK
    uk_cols = [c for c in merged.columns if c.endswith("_UK")]
    df_UK = merged[uk_cols].copy()
    df_UK = _drop_unwanted(df_UK, ["CPI_UK", "ExchRate_UK"])
    df_UK = _trade_balance(df_UK, "UK")
    df_UK = _move_gdp_last(df_UK, "GDP_UK")
    out["df_UK"] = df_UK

    # Japan
    jp_cols = [c for c in merged.columns if c.endswith("_JAPAN")]
    df_Japan = merged[jp_cols].copy()
    df_Japan = _drop_unwanted(df_Japan, ["CPI_JAPAN", "ExchRate_JAPAN"])
    df_Japan = _trade_balance(df_Japan, "JAPAN")
    df_Japan = _move_gdp_last(df_Japan, "GDP_JAPAN")
    out["df_Japan"] = df_Japan

    # China
    cn_cols = [c for c in merged.columns if c.endswith("_CHINA")]
    df_China = merged[cn_cols].copy()
    df_China = _drop_unwanted(df_China, ["CPI_CHINA", "ExchRate_CHINA"])
    df_China = _trade_balance(df_China, "CHINA")
    df_China = _move_gdp_last(df_China, "GDP_CHINA")
    out["df_China"] = df_China

    return out


# ---------------------------
# Entrypoint
# ---------------------------

# Expose globals the runner will auto-save
merged_df: pd.DataFrame
df_USA: pd.DataFrame
df_UK: pd.DataFrame
df_Japan: pd.DataFrame
df_China: pd.DataFrame


def main() -> None:
    global merged_df, df_USA, df_UK, df_Japan, df_China
    merged_df = build_merged()
    parts = split_by_country(merged_df)
    df_USA = parts["df_USA"]
    df_UK = parts["df_UK"]
    df_Japan = parts["df_Japan"]
    df_China = parts["df_China"]


# Execute immediately so the CLI runner sees the DataFrames as globals
main()
