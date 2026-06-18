import pandas as pd
import matplotlib as plt

data = {
    "age": [25, 30, 35, None, 40, 120, 29, 31],
    "income": [50000, 60000, 75000, 80000, None, 95000, 62000, 58000],
    "score": [85, 90, 78, 92, 88, None, 76, 95]
}

df = pd.DataFrame(data)

mean = df["age"].mean()
median = df["age"].median()

def summarize_data(df):
    stats = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            stats['mean'] = df[col].mean()
            stats['median'] = df[col].mean()

summarize_data(df)