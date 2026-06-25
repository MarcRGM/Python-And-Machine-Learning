import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

raw_data = load_data("sample_data.csv")
cleaned_df = clean_data(raw_data)
print(analyze_data(cleaned_df))