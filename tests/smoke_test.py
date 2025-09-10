import os, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1]
pipeline = HERE / "src" / "user_pipeline.py"
assert pipeline.exists(), "src/user_pipeline.py is missing"
# Ensure the file can be parsed
spec = importlib.util.spec_from_file_location("user_pipeline", pipeline)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print("OK: user_pipeline.py imports and executes module-level code without error.")
