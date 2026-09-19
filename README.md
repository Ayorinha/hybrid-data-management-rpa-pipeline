# Hybrid Data Management RPA Pipeline

A small, runnable data-validation pipeline designed as the foundation for RPA-ready operational workflows.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python pipeline.py sample.csv -o output/validated.csv
```

The example uses synthetic data only.

## Pipeline

```text
CSV/XLSX
   ↓
Schema validation
   ↓
Type normalization
   ↓
Status normalization
   ↓
Operational flags
   ↓
Validated CSV
```

This repository is intentionally a foundation, not a claim of direct access to institutional RPA systems.

## Author

**Anderson Leon Ayora** — Data Scientist | AI Engineer | Data Architect
