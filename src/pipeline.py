#!/usr/bin/env python
"""
Batch runner for your data cleaning & transformation pipeline.

Usage examples:
  python -m src.pipeline --input data/raw.csv --output-dir outputs
  python -m src.pipeline --input-dir data/raw --glob "*.csv" --output-dir outputs --save-vars "^(df|clean|final).*"

Environment/Globals injected before execution:
  - INPUT_FILE: path to current input file
  - OUTPUT_DIR: directory to save outputs for this run
  - CURRENT_BASENAME: base filename without extension

After executing the pipeline code, we automatically save any pandas.DataFrame variables in globals.
"""

import os, sys, re, json, runpy, traceback
from pathlib import Path

try:
    import pandas as pd
except Exception:
    pd = None

DEFAULT_SAVE_VARS = r"^(df$|df_.*|clean.*|final.*|.*_clean$|.*_final$)"

def save_namespace(ns, out_dir: Path, save_vars_pattern: str = DEFAULT_SAVE_VARS, fmt: str = "csv"):
    """Save DataFrame-like globals and common metrics to out_dir."""
    pattern = re.compile(save_vars_pattern)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save DataFrames
    if pd is not None:
        for name, obj in ns.items():
            if name.startswith("__"):
                continue
            if hasattr(obj, "to_csv") and isinstance(obj, pd.DataFrame):
                if not pattern.search(name):
                    continue
                fp = out_dir / f"{name}.{fmt}"
                try:
                    if fmt == "csv":
                        obj.to_csv(fp, index=False)
                    elif fmt == "parquet":
                        obj.to_parquet(fp, index=False)
                    else:
                        obj.to_csv(fp.with_suffix(".csv"), index=False)
                    print(f"[saved] DataFrame: {name} -> {fp}")
                except Exception as e:
                    print(f"[warn] Could not save DataFrame {name}: {e}")

    # Save common metrics/objects if present
    for mname in ["metrics", "metrics_df", "results", "summary", "report_df"]:
        obj = ns.get(mname)
        if obj is None:
            continue
        try:
            if pd is not None and isinstance(obj, pd.DataFrame):
                obj.to_csv(out_dir / f"{mname}.csv", index=False)
            else:
                # try JSON-serializable
                import json
                with open(out_dir / f"{mname}.json", "w", encoding="utf-8") as f:
                    json.dump(obj, f, default=str, indent=2)
            print(f"[saved] {mname}")
        except Exception as e:
            print(f"[warn] Could not save {mname}: {e}")

def run_once(pipeline_path: Path, input_file: Path, run_root: Path, save_vars_pattern: str, fmt: str):
    base = input_file.stem
    out_dir = run_root / base
    out_dir.mkdir(parents=True, exist_ok=True)

    # Prepare execution namespace
    ns = {
        "__name__": "__main__",
        "INPUT_FILE": str(input_file),
        "OUTPUT_DIR": str(out_dir),
        "CURRENT_BASENAME": base,
    }

    # Provide helpful prints so your code can use these
    print(f"[run] INPUT_FILE={input_file}")
    print(f"[run] OUTPUT_DIR={out_dir}")

    # Execute the pipeline code
    try:
        runpy.run_path(str(pipeline_path), init_globals=ns)
    except SystemExit:
        # allow scripts with argparse main() to call sys.exit
        pass
    except Exception as e:
        print("[error] Pipeline execution failed:", e)
        traceback.print_exc()

    # Save detected outputs
    save_namespace(ns, out_dir, save_vars_pattern=save_vars_pattern, fmt=fmt)

def main(argv=None):
    import argparse
    p = argparse.ArgumentParser(description="Batch-run your cleaning/transformation pipeline over many files.")
    p.add_argument("--pipeline", type=Path, default=Path("/mnt/data/dataframes-review/notebook_with_outputs.py") if True else None,
                   help="Path to the exported notebook script to execute for each file.")
    p.add_argument("--input", type=Path, help="Single input file path.")
    p.add_argument("--input-dir", type=Path, help="Directory of input files.")
    p.add_argument("--glob", default="*.csv", help="Glob for input-dir, e.g., *.csv or *.xlsx")
    p.add_argument("--output-dir", type=Path, default=Path("outputs/runs"), help="Root output directory.")
    p.add_argument("--fmt", choices=["csv","parquet"], default="csv", help="Format for saving DataFrames.")
    p.add_argument("--save-vars", default=DEFAULT_SAVE_VARS, help="Regex of variable names to auto-save as DataFrames.")
    args = p.parse_args(argv)

    if args.pipeline is None or not args.pipeline.exists():
        print("Error: pipeline script not found. Provide --pipeline path to your exported notebook code.")
        return 2

    files = []
    if args.input:
        files = [args.input]
    elif args.input_dir:
        files = sorted(args.input_dir.glob(args.glob))
    else:
        print("Error: provide --input FILE or --input-dir DIR [--glob PATTERN]")
        return 2

    if not files:
        print("No input files matched.")
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for f in files:
        run_once(args.pipeline, f, args.output_dir, save_vars_pattern=args.save_vars, fmt=args.fmt)

if __name__ == "__main__":
    sys.exit(main())
