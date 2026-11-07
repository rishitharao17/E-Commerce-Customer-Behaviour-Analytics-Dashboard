
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "clean_dataset.csv")

output_dir = BASE_DIR / "visualisation_outputs"
output_dir.mkdir(exist_ok=True)

# 1. Purchase distribution
purchase = df["Revenue"].value_counts().reset_index()
purchase.columns = ["Purchase", "Sessions"]
purchase["Purchase"] = purchase["Purchase"].map(
    {True: "Purchased", False: "Not Purchased",
     1: "Purchased", 0: "Not Purchased"}
)

fig = px.pie(
    purchase, names="Purchase", values="Sessions",
    title="Purchase vs Non-Purchase Distribution",
    hole=0.4
)
fig.write_html(output_dir / "purchase_distribution.html")

# 2. Visitor type analysis
visitor = df.groupby("VisitorType")["Revenue"].mean().reset_index()
visitor["Conversion_Rate"] = visitor["Revenue"] * 100

fig = px.bar(
    visitor, x="VisitorType", y="Conversion_Rate",
    title="Conversion Rate by Visitor Type",
    labels={"Conversion_Rate": "Conversion Rate (%)"}
)
fig.write_html(output_dir / "visitor_conversion.html")

# 3. Monthly conversion rate
monthly = df.groupby("Month")["Revenue"].mean().reset_index()
monthly["Conversion_Rate"] = monthly["Revenue"] * 100

fig = px.bar(
    monthly, x="Month", y="Conversion_Rate",
    title="Monthly Conversion Rate",
    labels={"Conversion_Rate": "Conversion Rate (%)"}
)
fig.write_html(output_dir / "monthly_conversion.html")

# 4. Weekend vs weekday
weekend = df.groupby("Weekend")["Revenue"].mean().reset_index()
weekend["Day_Type"] = weekend["Weekend"].map(
    {True: "Weekend", False: "Weekday"}
)
weekend["Conversion_Rate"] = weekend["Revenue"] * 100

fig = px.bar(
    weekend, x="Day_Type", y="Conversion_Rate",
    title="Weekend vs Weekday Conversion",
    labels={"Conversion_Rate": "Conversion Rate (%)"}
)
fig.write_html(output_dir / "weekend_conversion.html")

# 5. Product page duration vs purchase
fig = px.box(
    df, x="Revenue", y="ProductRelated_Duration",
    title="Product Page Duration vs Purchase",
    labels={
        "Revenue": "Purchase Status",
        "ProductRelated_Duration": "Duration (seconds)"
    }
)
fig.write_html(output_dir / "product_engagement.html")

print("All visualisations created successfully!")
print("Saved in:", output_dir)
