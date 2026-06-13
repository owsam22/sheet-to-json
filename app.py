from pathlib import Path
import pandas as pd
import json

DATA_DIR = Path("data")
RESULT_DIR = Path("result")

# Create result folder if it doesn't exist
RESULT_DIR.mkdir(exist_ok=True)

# Process every Excel file in data folder
for excel_file in DATA_DIR.glob("*.xlsx"):

    if excel_file.name.startswith("~$"):
        # Skip temporary files created by Excel
        continue

    df = pd.read_excel(excel_file)

    data = df.to_dict(orient="records")

    output_file = RESULT_DIR / f"{excel_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Generated: {output_file.name}")

print("All files converted successfully.")