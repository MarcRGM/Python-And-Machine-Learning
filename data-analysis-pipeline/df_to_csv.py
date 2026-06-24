import pandas as pd

data = {
    "age": [25, 30, 35, None, 40, 120, 29, 31],
    "income": [50000, 60000, 75000, 80000, None, 95000, 62000, 58000],
    "score": [85, 90, 78, 92, 88, None, 76, 95]
}

def convert_csv(data):
    pd.DataFrame(data).to_csv('sample_data.csv', index=False)

convert_csv(data)

