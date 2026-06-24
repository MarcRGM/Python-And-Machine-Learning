import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(csv):
    file_name = csv + ".csv"
    return pd.read_csv(file_name)

print(load_data("sample_data"))
