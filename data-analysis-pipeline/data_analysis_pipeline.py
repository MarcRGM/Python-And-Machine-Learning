import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

raw_data = load_data("sample_data.csv")
