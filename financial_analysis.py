```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

data = {
    "year": [2021, 2022, 2023, 2024],
    "revenue": [2200, 2500, 2750, 3100],
    "cost": [1200, 1350, 1480, 1650],
    "net_profit": [210, 245, 280, 330],
    "total_asset": [3500, 3800, 4100, 4500],
    "total_liability": [1600, 1720, 1800, 1930]
}
df = pd.DataFrame(data)

df["gross_margin"] = (df["revenue"] - df["cost"]) / df["revenue"]
df["roe"] = df["net_profit"] / df["total_asset"]
df["debt_ratio"] = df["total_liability"] / df["total_asset"]

print("===== 财务指标结果 =====")
print(df[["year","gross_margin","roe","debt_ratio"]].round(4))

plt.figure(figsize=(10,5))
plt.plot(df["year"], df["gross_margin"], marker='o', label="毛利率")
plt.plot(df["year"], df["roe"], marker='s', label="ROE")
plt.plot(df["year"], df["debt_ratio"], marker='^', label="资产负债率")
plt.xlabel("年份")
plt.ylabel("比率")
plt.title("企业历年财务指标趋势")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("financial_chart.png", dpi=300)
plt.show()
