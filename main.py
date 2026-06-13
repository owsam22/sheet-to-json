from tkinter import Tk, filedialog, messagebox
from pathlib import Path
import pandas as pd
import json

# Hide tkinter root window
root = Tk()
root.withdraw()

# Create result folder if not exists
RESULT_DIR = Path("result")
RESULT_DIR.mkdir(exist_ok=True)

# Select excel files
files = filedialog.askopenfilenames(
    title="Select Excel Files",
    filetypes=[("Excel Files", "*.xlsx *.xls")]
)

if not files:
    print("No files selected.")
    exit()

for file in files:
    

    excel_file = Path(file)
    if excel_file.name.startswith("~$"):
        # Skip temporary files created by Excel
        continue

    # Read excel
    df = pd.read_excel(excel_file)

    # Convert to JSON
    data = df.to_dict(orient="records")

    # Save in result folder
    output_file = RESULT_DIR / f"{excel_file.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    print(f"Generated: {output_file}")

messagebox.showinfo(
    "Success",
    f"{len(files)} file(s) converted successfully."
)