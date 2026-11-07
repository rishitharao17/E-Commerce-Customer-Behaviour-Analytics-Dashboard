# 📥 Data Collection

## 🛍️ Project
**E-Commerce Customer Behaviour Analytics Dashboard**

## 🎯 Objective
To obtain the **Online Shoppers Purchasing Intention** dataset and load it into Python for inspection and subsequent analysis.

## 📊 Dataset Details
- **Dataset name:** Online Shoppers Purchasing Intention
- **Source:** Kaggle
- **Dataset link:** https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset
- **Original source:** UCI Machine Learning Repository
- **Documented size:** 12,330 shopping sessions and 18 attributes
- **Target attribute:** `Revenue`, which indicates whether a shopping session resulted in a purchase
- **Tools:** Python, Google Colab, Pandas

## 🧭 Data Collection Procedure
1. Open the dataset page on Kaggle.
2. Download the dataset archive.
3. Upload the ZIP file to Google Colab.
4. Extract the archive and identify the CSV file.
5. Load the CSV file into a Pandas DataFrame.
6. Inspect the dimensions, column names, and first few records.

## 💻 Example Python Code

```python
from google.colab import files
uploaded = files.upload()
```

If the uploaded file is a ZIP archive, extract it:

```python
import zipfile
from pathlib import Path

zip_files = [
    name for name in uploaded
    if name.lower().endswith(".zip")
]

if zip_files:
    with zipfile.ZipFile(zip_files[0], "r") as zip_ref:
        zip_ref.extractall("/content/ecommerce_data")

csv_files = list(
    Path("/content/ecommerce_data").rglob("*.csv")
)

for file in csv_files:
    print(file)
```

Load the selected CSV file. If the ZIP contains more than one CSV, choose the correct file first.

```python
import pandas as pd

# Run this only when exactly one CSV file was found.
if len(csv_files) == 1:
    df = pd.read_csv(csv_files[0])
    print("Dataset shape:", df.shape)
    print("Column names:", df.columns.tolist())
    display(df.head())
else:
    print("Select the correct CSV file from the list above.")
```

## 📋 Collection Record
Fill in these details after completing the process.

- **Date collected:** To be recorded
- **CSV filename:** To be recorded
- **Rows and columns reported by Colab:** To be confirmed
- **Collection status:** To be updated after successful loading

## ✅ Outcome
The dataset is collected and loaded into a Pandas DataFrame, ready for data-quality checks and cleaning.

**Next stage:** 🧹 Data Cleaning
