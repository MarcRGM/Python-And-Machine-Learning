# NumPy Vector Explorer

A lightweight Python tool that demonstrates fundamental **NumPy operations** for
machine learning data preparation. It creates arrays from raw data, computes
summary statistics while handling missing values, and performs vectorized
arithmetic.

## Features
- Convert dictionary data to NumPy arrays with proper NaN handling
- Compute mean, median, standard deviation, min, max while ignoring missing values
- Count missing values per array
- Demonstrate vectorized addition on entire arrays

## Usage
python

import numpy as np

from numpy_vector_explorer import array_summary, compare_ages

age = np.array([25, 30, 35, None, 40, 120, 29, 31], dtype=float)

stats = array_summary(age)

print(stats)

current, future = compare_ages(age)

print(f"Mean ages: {current}, {future}")

## Technologies
- **Python 3.x**
- **NumPy**

## Background
- Numerical computing fundamentals
- NaN‑aware statistical functions
- Vectorized operations (the core performance advantage of NumPy)