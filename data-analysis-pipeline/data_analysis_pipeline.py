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

def clean_data(df):
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].mean())
    return df

def analyze_data(df):
    summary = {}
    for col in df.select_dtypes(include="number").columns:
        np_data = {}
        np_list = np.array(df[col], dtype=float)
        np_data["mean"] = np.nanmean(np_list)
        np_data["median"]= np.nanmedian(np_list)
        np_data["std"] = np.nanstd(np_list)
        np_data["min"] = np.nanmin(np_list)
        np_data["max"] = np.nanmax(np_list)
        np_data["missing_count"] = np.isnan(np_list).sum()
        summary[col] = np_data
    return summary

def plot_distribution(df):
    for col in df.select_dtypes(include="number").columns:
        plt.hist(df[col], 4)
        plt.title(f"{col} distribution")
        plt.xlabel(col)
        plt.ylabel("frequency")
        plt.savefig(col)

def export_report(summary, df):
    report_lines = []
    report_lines.append("Data Analysis Report")
    report_lines.append(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    for col in summary:
        report_lines.append(f"{col} = {summary[col]}")
    report_lines.append("Histograms: age.png, income.png, and score.png")

    with open("report.txt", "w") as f:
        f.write("\n".join(report_lines))

convert_csv(data)
raw_data = load_data("sample_data.csv")
cleaned_df = clean_data(raw_data)
plot_distribution(cleaned_df)
export_report(analyze_data(cleaned_df), cleaned_df)