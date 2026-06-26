# Data Analysis Pipeline

A modular data analysis pipeline built with Python. It loads a CSV file,
cleans missing values, computes summary statistics with NumPy, generates
histograms, and exports a text report.

## Features
- CSV generation from raw data
- Missing‑value handling with median imputation
- Summary statistics (mean, median, std, min, max, missing counts)
- Histogram export as PNG files
- Text report generation with dynamic content

## Usage
python data_analysis_pipeline.py

Output: `report.txt`, `histograms/age.png`, `histograms/income.png`, `histograms/score.png`

## Technologies
- Python 3.x
- pandas
- NumPy
- matplotlib

## Background
- Multi‑step pipeline architecture
- Outlier‑aware imputation (median over mean)
- Organized output management (subdirectories)
- Dynamic report generation