# 🧹 Data Cleaning

## 🎯 Objective
To examine the collected Online Shoppers Purchasing Intention dataset for data-quality issues and prepare it for analysis without making unnecessary changes to valid data.

## 🛠️ Tools
- Python
- Pandas
- Google Colab

## 🔍 Data Cleaning Procedure

### 1. Inspect the dataset
Check the dataset dimensions, first records, and column data types.

```python
print("Dataset shape:", df.shape)
display(df.head())
print(df.dtypes)
```

### 2. Check missing values

```python
print("Missing values by column:")
print(df.isnull().sum())

print("Total missing values:", df.isnull().sum().sum())
```

If missing values are present, investigate which columns contain them and choose an appropriate treatment based on the data. Do not automatically remove rows without checking the impact.

### 3. Check duplicate rows

```python
print("Duplicate rows:", df.duplicated().sum())
```

Investigate duplicates before removing them. Identical rows are not always proof of an invalid record, particularly when each row represents a session.

### 4. Inspect data types

```python
print(df.dtypes)
```

Confirm that numerical, categorical, and Boolean attributes use suitable types. Convert types only when the actual values and analysis requirements justify it.

### 5. Inspect important categorical values

```python
print("Revenue values:")
print(df["Revenue"].value_counts(dropna=False))

print("\nVisitor types:")
print(df["VisitorType"].value_counts(dropna=False))

print("\nMonths:")
print(df["Month"].value_counts(dropna=False))
```

Look for unexpected values and inconsistent labels. Correct only issues confirmed by inspection.

### 6. Save the verified dataset

After completing and documenting any required corrections:

```python
output_path = "/content/cleaned_online_shoppers.csv"
df.to_csv(output_path, index=False)

print("Saved:", output_path)
print("Final shape:", df.shape)
```

## 📋 Data Cleaning Results

Complete this table using the actual output from Google Colab.

| Check | Actual result |
|---|---|
| Initial dimensions | 12,330 rows × 18 columns, as shown in the current Colab screenshot |
| Total missing values | To be confirmed from the complete output |
| Duplicate rows | To be confirmed |
| Data types reviewed | To be confirmed |
| Corrections performed | Record only corrections actually made |
| Final dimensions | To be confirmed after any corrections |

## ⚠️ Important Notes
- A check is not the same as a correction. Document what was actually found and changed.
- Do not claim the entire dataset has zero missing values until the full output confirms it.
- Do not remove duplicate rows unless you have decided they are invalid for this analysis.
- Keep the original downloaded dataset unchanged so the cleaning process is reproducible.
- Avoid uploading the raw dataset to a public GitHub repository unless its licence and sharing terms permit it.

## ✅ Outcome
The data-quality checks and any justified corrections prepare the dataset for exploratory data analysis and KPI calculation.

**Next stage:** 📊 Data Analytics
