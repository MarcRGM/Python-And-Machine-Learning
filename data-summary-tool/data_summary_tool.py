import pandas as pd
import matplotlib.pyplot as plt

data = {
    "age": [25, 30, 35, None, 40, 120, 29, 31],
    "income": [50000, 60000, 75000, 80000, None, 95000, 62000, 58000],
    "score": [85, 90, 78, 92, 88, None, 76, 95]
}

df = pd.DataFrame(data)

def summarize_data(df):
    col_stats = {}
    for col in df.columns:
        stats = {}
        if pd.api.types.is_numeric_dtype(df[col]):
            stats['mean'] = df[col].mean()
            stats['median'] = df[col].median()
            stats['std'] = df[col].std()
            stats['min'] = df[col].min()
            stats['max'] = df[col].max()
            stats['missing_values'] = df[col].isnull().sum()
            col_stats[col] = stats
    return col_stats

def plot_histograms(df, bins=4):
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.hist(df[col].dropna(), bins=4)
            plt.title(f"{col} distribution")
            plt.xlabel(f"{col}")
            plt.ylabel("frequency")
            plt.show()
    return None

print(summarize_data(df))
plot_histogram(df)