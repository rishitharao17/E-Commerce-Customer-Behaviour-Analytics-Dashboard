
import pandas as pd
from pathlib import Path

# Load cleaned dataset
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "clean_dataset.csv")

# Create output folder
output_dir = BASE_DIR / "analysis_outputs"
output_dir.mkdir(exist_ok=True)

print("\n===== E-COMMERCE DATA ANALYSIS =====")

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Total sessions:", len(df))
print("Total columns:", len(df.columns))

# 2. Purchase analysis
print("\n2. PURCHASE ANALYSIS")

total_sessions = len(df)
purchase_sessions = int(df["Revenue"].sum())
non_purchase_sessions = total_sessions - purchase_sessions

conversion_rate = purchase_sessions / total_sessions * 100

print("Total sessions:", total_sessions)
print("Purchase sessions:", purchase_sessions)
print("Non-purchase sessions:", non_purchase_sessions)
print("Conversion rate:", round(conversion_rate, 2), "%")

# 3. Visitor type analysis
print("\n3. VISITOR TYPE ANALYSIS")

visitor_analysis = df.groupby("VisitorType", observed=True).agg(
    Total_Sessions=("Revenue", "count"),
    Purchases=("Revenue", "sum")
)

visitor_analysis["Conversion_Rate"] = (
    visitor_analysis["Purchases"] /
    visitor_analysis["Total_Sessions"] * 100
).round(2)

print(visitor_analysis)
visitor_analysis.to_csv(output_dir / "visitor_analysis.csv")

# 4. Monthly analysis
print("\n4. MONTHLY PURCHASE ANALYSIS")

monthly_analysis = df.groupby("Month", observed=True).agg(
    Total_Sessions=("Revenue", "count"),
    Purchases=("Revenue", "sum")
)

monthly_analysis["Conversion_Rate"] = (
    monthly_analysis["Purchases"] /
    monthly_analysis["Total_Sessions"] * 100
).round(2)

print(monthly_analysis)
monthly_analysis.to_csv(output_dir / "monthly_analysis.csv")

# 5. Weekend analysis
print("\n5. WEEKEND VS WEEKDAY ANALYSIS")

weekend_analysis = df.groupby("Weekend", observed=True).agg(
    Total_Sessions=("Revenue", "count"),
    Purchases=("Revenue", "sum")
)

weekend_analysis["Conversion_Rate"] = (
    weekend_analysis["Purchases"] /
    weekend_analysis["Total_Sessions"] * 100
).round(2)

print(weekend_analysis)
weekend_analysis.to_csv(output_dir / "weekend_analysis.csv")

# 6. Website engagement
print("\n6. WEBSITE ENGAGEMENT")

engagement = df[
    ["Administrative_Duration", "Informational_Duration",
     "ProductRelated_Duration", "BounceRates",
     "ExitRates", "PageValues"]
].describe().round(2)

print(engagement)
engagement.to_csv(output_dir / "engagement_statistics.csv")

# 7. Final summary
print("\n===== ANALYSIS COMPLETED =====")
print("Most common visitor type:", df["VisitorType"].mode()[0])
print("Average product page duration:",
      round(df["ProductRelated_Duration"].mean(), 2))

print("Analysis files saved in:", output_dir)



#output
'''===== E-COMMERCE DATA ANALYSIS =====

1. DATASET OVERVIEW
Total sessions: 12205
Total columns: 18

2. PURCHASE ANALYSIS
Total sessions: 12205
Purchase sessions: 1908
Non-purchase sessions: 10297
Conversion rate: 15.63 %

3. VISITOR TYPE ANALYSIS
                   Total_Sessions  Purchases  Conversion_Rate
VisitorType                                                  
New_Visitor                  1693        422            24.93
Other                          81         16            19.75
Returning_Visitor           10431       1470            14.09

4. MONTHLY PURCHASE ANALYSIS
       Total_Sessions  Purchases  Conversion_Rate
Month                                            
Aug               433         76            17.55
Dec              1706        216            12.66
Feb               181          3             1.66
Jul               432         66            15.28
June              285         29            10.18
Mar              1860        192            10.32
May              3329        365            10.96
Nov              2982        760            25.49
Oct               549        115            20.95
Sep               448         86            19.20

5. WEEKEND VS WEEKDAY ANALYSIS
         Total_Sessions  Purchases  Conversion_Rate
Weekend                                            
False              9346       1409            15.08
True               2859        499            17.45

6. WEBSITE ENGAGEMENT
       Administrative_Duration  Informational_Duration  ProductRelated_Duration  BounceRates  ExitRates  PageValues
count                 12205.00                12205.00                 12205.00     12205.00   12205.00    12205.00
mean                     81.65                   34.83                  1206.98         0.02       0.04        5.95
std                     177.49                  141.42                  1919.60         0.05       0.05       18.65
min                       0.00                    0.00                     0.00         0.00       0.00        0.00
25%                       0.00                    0.00                   193.00         0.00       0.01        0.00
50%                       9.00                    0.00                   608.94         0.00       0.02        0.00
75%                      94.70                    0.00                  1477.15         0.02       0.05        0.00
max                    3398.75                 2549.38                 63973.52         0.20       0.20      361.76

===== ANALYSIS COMPLETED ===== '''
