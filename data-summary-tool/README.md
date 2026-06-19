# Data Summary Tool

A lightweight Python tool for **exploratory data analysis (EDA)**. It computes
descriptive statistics (mean, median, standard deviation, min, max, missing
values) for every numeric column of a dataset and visualises the distributions
with histograms.

## Features
- Summarise any Pandas DataFrame with one function call.
- Separate functions for statistics and plotting.
- Count missing values per column.
- Easily adjustable histogram bin size.

## Usage
import pandas as pd
from data_summary_tool import summarize_data, plot_histograms
df = pd.read_csv('your_data.csv')
stats = summarize_data(df)
print(stats)
plot_histograms(df)

## Technologies
- **Python 3.x**
- **Pandas**
- **Matplotlib**

## Background
- Python fundamentals (functions, loops, dictionaries)
- Data loading and cleaning with Pandas
- Descriptive statistics
- Data visualisation