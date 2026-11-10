# 🛍️ E-Commerce Customer Behaviour Analytics Dashboard

<p align="center">
  <strong>📊 Turning online shopping session data into meaningful insights</strong><br>
  Built with Python, Pandas, Plotly, and PowerBI
</p>

---

## 🌟 About the Project

E-commerce websites collect useful information about how visitors browse products, interact with pages, and complete purchases. Understanding these patterns can help businesses make better data-informed decisions.

This project analyses the **Online Shoppers Purchasing Intention** dataset and presents findings through an interactive dashboard. It explores browsing behaviour and purchasing outcomes using Python-based data analysis and visualization tools.

## 🎯 Project Objectives

- 📥 Collect and inspect the online shopping dataset.
- 🧹 Clean and prepare the data for analysis.
- 🔎 Explore browsing activity and purchasing patterns.
- 📈 Calculate relevant metrics and compare purchase outcomes.
- 📊 Build clear, interactive charts and visualizations.
- 💡 Present findings that can support e-commerce decision-making.
   
## 📂 Dataset

- **Dataset:** Online Shoppers Purchasing Intention
- **Source:** [Kaggle — Online Shoppers Purchasing Intention](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)
- **Original source:** UCI Machine Learning Repository
- **Documented size:** 12,330 shopping sessions and 18 attributes
- **Purchase indicator:** `Revenue`

The dataset includes information about page visits and durations, bounce and exit rates, page values, month, visitor type, weekend status, and other session characteristics.

> ⚠️ **Important:** `Revenue` indicates whether a session resulted in a purchase; it is not the monetary amount of a sale. `PageValues` is a separate metric in the dataset.

## 🧭 Project Workflow

The project follows the five stages specified for the course.

### 1️⃣ 📝 Project Proposal
Define the problem statement, objectives, scope, technology stack, methodology, and expected outcomes.

### 2️⃣ 📥 Data Collection
Download the dataset from Kaggle, extract the CSV file, and load it into Python using Pandas.

### 3️⃣ 🧹 Data Cleaning
Check for missing values, duplicate records, incorrect data types, inconsistent categories, and other data-quality issues. Apply suitable corrections based on the actual data.

### 4️⃣ 🔍 Data Analytics
Perform exploratory data analysis and calculate useful metrics, such as session counts and purchase conversion rate. Compare browsing patterns across relevant customer and session groups.

### 5️⃣ 📊 Data Visualization
Use Plotly to create interactive charts and PowerBI to bring the results together in an easy-to-use dashboard.

## 🛠️ Technology Stack

| Tool | Purpose |
|---|---|
| 🐍 Python | Programming and analysis |
| 🐼 Pandas | Data manipulation and analysis |
| 🔢 NumPy | Numerical operations |
| 📊 Plotly | Interactive visualizations |
| 📈 PowerBI | Dashboard interface |
| ☁️ Google Colab | Initial data exploration |
| 💻 Visual Studio Code | Local development |

## 📌 Planned Dashboard Features

The final features will depend on the columns and results confirmed during analysis.

- 📍 KPI cards for total sessions, purchase sessions, and non-purchase sessions
- 🛒 Purchase versus non-purchase comparisons
- ⏱️ Browsing engagement and page-duration analysis
- 👥 Comparisons by visitor type
- 📅 Analysis by month and weekend status
- 🎛️ Interactive filters for supported dataset attributes
- 💡 Concise findings grounded in the analysis

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your actual repository URL and folder name.

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

### 3. Install dependencies

Create a `requirements.txt` file with:

```text
pandas
numpy
plotly
POWERBI
```

Install the packages:

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

Download the CSV from the [Kaggle dataset page](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset).

Keep the file in your project's data folder, for example:

```text
data/online_shoppers_intention.csv
```

Make sure the filename in your code matches the file you downloaded. Check the dataset's licence and terms before redistributing it, and avoid committing large raw datasets to GitHub unless permitted and necessary.

### 5. Run the dashboard

After creating the POWERBI application and saving it as `app.py`, run:

```bash
POWERBI run app.py
```

Open the local URL shown in the terminal to view the dashboard.

## 📁 Suggested Repository Structure

```text
ecommerce-customer-behaviour-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── .gitkeep
├── notebooks/
│   └── data_exploration.ipynb
└── outputs/
    └── .gitkeep
```

This is a suggested structure. Add files as the project develops, and do not include dataset filenames that do not match your actual files.

## 📐 Example KPI: Purchase Conversion Rate

The purchase conversion rate is the percentage of shopping sessions where `Revenue` is `True`.

```python
conversion_rate = df["Revenue"].mean() * 100
print(f"Purchase conversion rate: {conversion_rate:.2f}%")
```

This calculation assumes that `Revenue` contains Boolean values or equivalent `0`/`1` values. Check the column's data type and values before using it.

## ✅ Project Status

- [✅] Dataset selected
- [✅] Project proposal drafted
- [✅] Dataset downloaded and loaded
- [✅] Data quality checks completed
- [ ] Data cleaning documented
- [ ] Exploratory data analysis completed
- [ ] KPIs and visualizations implemented
- [ ] POWERBI dashboard developed
- [ ] Dashboard tested and deployed

## 🎓 Expected Outcome

The completed project will provide an interactive way to explore online shopping sessions, compare purchasing outcomes, and investigate browsing patterns associated with purchases. The results can help users understand the dataset and support data-informed e-commerce decisions.

> 📌 **Note:** Observed relationships do not, by themselves, prove that a particular browsing behaviour causes a purchase.

## 🙌 Acknowledgements

- 📊 Dataset: [Online Shoppers Purchasing Intention — Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)
- 🏛️ Original dataset source: UCI Machine Learning Repository

---

<p align="center">
  ⭐ <strong>E-Commerce Customer Behaviour Analytics Dashboard</strong><br>
  📚 Course: Data Analytics and Visualization
</p>
