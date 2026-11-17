import pandas as pd

# 1. 造一个小表格
data = {
    "company": ["A公司", "B公司", "C公司"],
    "revenue": [5000, 7200, 3800],
    "cost": [3000, 4500, 2200]
}

# 2. 转成Pandas表格（DataFrame）
df = pd.DataFrame(data)
print("原始表格：")
print(df)

# 3. 新增毛利率列
df["gross_margin"] = (df["revenue"] - df["cost"]) / df["revenue"]
print("\n加上毛利率之后：")
print(df)

# 4. 筛选毛利率大于40%的公司
high_margin = df[df["gross_margin"] > 0.4]
print("\n毛利率>40%的公司：")
print(high_margin)
