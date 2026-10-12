E-Commerce Customer Behaviour Analytics Dashboard
An interactive data analytics dashboard that explores online shopping sessions and purchasing behaviour using the Online Shoppers Purchasing Intention dataset from Kaggle.
The project uses Python for data processing and analysis, Plotly for interactive visualizations, and Streamlit to build the dashboard.
Project Objectives
- Explore online shopping session data.
- Clean and prepare the dataset for analysis.
- Analyse browsing activity and purchasing outcomes.
- Compare purchase and non-purchase sessions.
- Visualize relevant metrics and patterns in an interactive dashboard.
- Present findings that can support data-informed e-commerce decisions.
Dataset
- Name: Online Shoppers Purchasing Intention
- Source: Kaggle — Online Shoppers Purchasing Intention Dataset
- Original source: UCI Machine Learning Repository
- Size: 12,330 sessions and 18 attributes, according to the dataset documentation.
- Target attribute: Revenue — indicates whether a shopping session resulted in a purchase.
The dataset includes session characteristics such as page visits and durations, bounce and exit rates, page values, month, visitor type, weekend status, and other browsing-related attributes.
Note: Revenue is a purchase indicator, not a transaction amount. Do not interpret it as the monetary value of a sale. PageValues is a separate dataset attribute.

Project Workflow
The project follows these five stages:
1. Project Proposal — define the problem, objectives, scope, tools, and expected outcomes.
2. Data Collection — download the dataset and load the CSV into Python.
3. Data Cleaning — inspect and address missing values, duplicate records, data types, and data-quality issues as appropriate.
4. Data Analytics — perform exploratory analysis and calculate relevant metrics, such as session counts and purchase conversion rate.
5. Data Visualization — present findings through Plotly charts and an interactive Streamlit dashboard.
Technology Stack
- Python — programming language
- Pandas — data manipulation and analysis
- NumPy — numerical operations
- Plotly — interactive charts
- Streamlit — dashboard interface
- Google Colab — initial data exploration
- Visual Studio Code — local development
Planned Dashboard Features
The final features will depend on the columns and results confirmed during analysis.
- KPI cards for total sessions, purchase sessions, non-purchase sessions, and purchase conversion rate
- Purchase versus non-purchase comparisons
- Browsing engagement and page-duration analysis
- Comparisons by visitor type, month, and weekend status
- Interactive filters for supported dataset attributes
- Clear charts and concise analytical findings
Getting Started
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
Replace the placeholders with your actual GitHub repository URL and folder name.
2. Create and activate a virtual environment
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Windows
python -m venv .venv
.venv\\Scripts\\activate
3. Install dependencies
Create a requirements.txt file containing:
pandas
numpy
plotly
streamlit
Then run:
pip install -r requirements.txt
4. Add the dataset
Download the CSV from Kaggle. Place it in your project data folder, for example:
data/online_shoppers_intention.csv
The filename and path in your Python code must match the file you actually use. Check the dataset's licence and terms before redistributing it. Avoid committing large raw datasets to GitHub unless permitted and necessary.
5. Run the dashboard
Once the Streamlit application has been implemented and saved as app.py, run:
streamlit run app.py
Streamlit will provide a local URL in the terminal where you can open the dashboard.
Suggested Repository Structure
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
This is a suggested structure; files and folders can be added as the project develops. Do not add the dataset filename above unless it matches your actual file.
Key Metric
Purchase Conversion Rate
The purchase conversion rate is the percentage of sessions where Revenue is True.
conversion_rate = df["Revenue"].mean() * 100
print(f"Purchase conversion rate: {conversion_rate:.2f}%")
This calculation assumes Revenue is represented as Boolean values or equivalent 0/1 values. Confirm the column's data type and values before using it.
Current Status
- [x] Dataset selected
- [x] Project proposal drafted
- [ ] Dataset downloaded and loaded
- [ ] Data quality checks completed
- [ ] Data cleaning documented
- [ ] Exploratory data analysis completed
- [ ] KPIs and visualizations implemented
- [ ] Streamlit dashboard completed
- [ ] Dashboard tested and deployed
Expected Outcome
The completed project will provide an interactive way to explore online shopping sessions, compare purchasing outcomes, and investigate browsing patterns associated with purchases. Findings will be based on the dataset and will not, by themselves, establish that a particular behaviour causes a purchase.
Acknowledgements
- Dataset: Online Shoppers Purchasing Intention — Kaggle
- Original dataset source: UCI Machine Learning Repository
Project: E-Commerce Customer Behaviour Analytics Dashboard
Course: Data Analytics and Visualization
