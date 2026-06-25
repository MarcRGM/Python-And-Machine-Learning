import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].mean())
    return df

raw_data = load_data("sample_data.csv")
cleaned_df = clean_data(raw_data)
print(cleaned_df.describe())