
import pandas as pd
from pathlib import Path

# --------------------------------
# 1. Define dataset paths
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent

input_file = BASE_DIR / "online_shoppers_intention 2.csv"
output_file = BASE_DIR / "clean_dataset.csv"

# --------------------------------
# 2. Load original dataset
# --------------------------------

print("Loading original dataset...")

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# --------------------------------
# 3. Check missing values
# --------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# --------------------------------
# 4. Check duplicate records
# --------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate records found:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate records removed.")

# --------------------------------
# 5. Check and clean data types
# --------------------------------

df.columns = df.columns.str.strip()

boolean_columns = ["Weekend", "Revenue"]

for col in boolean_columns:
    df[col] = df[col].astype("bool")

df["Month"] = df["Month"].astype("category")
df["VisitorType"] = df["VisitorType"].astype("category")

# --------------------------------
# 6. Validate numeric columns
# --------------------------------

numeric_columns = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="raise")

# --------------------------------
# 7. Check invalid values
# --------------------------------

assert df["BounceRates"].between(0, 1).all()
assert df["ExitRates"].between(0, 1).all()
assert df["SpecialDay"].between(0, 1).all()

assert df["Revenue"].notna().all()
assert df["Weekend"].notna().all()

# --------------------------------
# 8. Final missing value check
# --------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------
# 9. Save cleaned dataset
# --------------------------------

df.to_csv(output_file, index=False)

print("\nCleaning completed successfully!")
print("Final dataset shape:", df.shape)
print("Cleaned dataset saved at:", output_file)

#output:
'''
Original dataset shape: (12330, 18)

Missing values before cleaning:
Administrative             0
Administrative_Duration    0
Informational              0
Informational_Duration     0
ProductRelated             0
ProductRelated_Duration    0
BounceRates                0
ExitRates                  0
PageValues                 0
SpecialDay                 0
Month                      0
OperatingSystems           0
Browser                    0
Region                     0
TrafficType                0
VisitorType                0
Weekend                    0
Revenue                    0
dtype: int64

Duplicate records found: 125
Duplicate records removed.

Missing values after cleaning:
Administrative             0
Administrative_Duration    0
Informational              0
Informational_Duration     0
ProductRelated             0
ProductRelated_Duration    0
BounceRates                0
ExitRates                  0
PageValues                 0
SpecialDay                 0
Month                      0
OperatingSystems           0
Browser                    0
Region                     0
TrafficType                0
VisitorType                0
Weekend                    0
Revenue                    0
dtype: int64

Cleaning completed successfully!
Final dataset shape: (12205, 18)
'''
