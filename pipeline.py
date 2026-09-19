from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"record_id", "status", "amount"}

def run(input_path: Path, output_path: Path) -> pd.DataFrame:
    df = pd.read_excel(input_path) if input_path.suffix.lower() in {".xlsx", ".xls"} else pd.read_csv(input_path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.copy()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    df["status"] = df["status"].astype("string").str.strip().str.upper()
    df["is_pending"] = df["status"].eq("PENDING")
    df["is_valid"] = df["record_id"].notna() & df["status"].notna()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df

def main() -> None:
    parser = argparse.ArgumentParser(description="AYORAI hybrid data validation/RPA-ready pipeline")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("output/validated.csv"))
    args = parser.parse_args()
    df = run(args.input, args.output)
    print(f"Processed: {len(df)} records")
    print(f"Valid: {int(df['is_valid'].sum())}")
    print(f"Pending: {int(df['is_pending'].sum())}")

if __name__ == "__main__":
    main()
