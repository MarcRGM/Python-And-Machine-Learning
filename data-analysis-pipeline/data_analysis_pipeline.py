import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "age": [25, 30, 35, None, 40, 120, 29, 31],
    "income": [50000, 60000, 75000, 80000, None, 95000, 62000, 58000],
    "score": [85, 90, 78, 92, 88, None, 76, 95]
}

def convert_csv(data):
    pd.DataFrame(data).to_csv('sample_data.csv', index=False)

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(raw_df):
    df = raw_df.copy() # preserve raw_data
    missing_counts = {}
    for col in df.select_dtypes(include="number").columns:
        missing_counts[col] = df[col].isnull().sum()
        df[col] = df[col].fillna(df[col].median()) # median over mean to accomodate outliers
    return df, missing_counts

def analyze_data(df, missing_values):
    summary = {}
    for col in df.select_dtypes(include="number").columns:
        np_data = {}
        np_list = np.array(df[col], dtype=float)
        np_data["mean"] = np.nanmean(np_list)
        np_data["median"]= np.nanmedian(np_list)
        np_data["std"] = np.nanstd(np_list)
        np_data["min"] = np.nanmin(np_list)
        np_data["max"] = np.nanmax(np_list)
        np_data["missing_count"] = missing_counts[col] # np.isnan(np_list).sum() returns 0 since it was already cleaned from clean_data()
        summary[col] = np_data
    return summary

def plot_distribution(df):
    for col in df.select_dtypes(include="number").columns:
        plt.hist(df[col], 4)
        plt.title(f"{col} distribution")
        plt.xlabel(col)
        plt.ylabel("frequency")
        plt.savefig(f"{col}.png")
        plt.close()

def export_report(summary, df):
    report_lines = []
    report_lines.append("Data Analysis Report")
    report_lines.append(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    for col in summary:
        report_lines.append(f"{col} = {summary[col]}")
    report_lines.append("Histograms:")
    for col in df.columns:
        report_lines.append(f"{col}.png")
    with open("report.txt", "w") as f:
        f.write("\n".join(report_lines))

convert_csv(data)
raw_data = load_data("sample_data.csv")
cleaned_df, missing_counts = clean_data(raw_data)
plot_distribution(cleaned_df)
export_report(analyze_data(cleaned_df, missing_counts), cleaned_df)