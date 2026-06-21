import numpy as np

data = {
    "age": [25, 30, 35, None, 40, 120, 29, 31],
    "income": [50000, 60000, 75000, 80000, None, 95000, 62000, 58000],
    "score": [85, 90, 78, 92, 88, None, 76, 95]
}

age = np.array(data["age"], dtype=float)
income = np.array(data["income"], dtype=float)
score = np.array(data["score"], dtype=float)

def array_summary(arr):
    summary = {}
    summary["mean"] = np.nanmean(arr)
    summary["median"]= np.nanmedian(arr)
    summary["std"] = np.nanstd(arr)
    summary["min"] = np.nanmin(arr)
    summary["max"] = np.nanmax(arr)
    summary["missing_count"] = np.isnan(arr).sum()
    return summary

def compare_ages(age):
    current_age_mean = np.nanmean(age)
    future_age_mean = np.nanmean(age+10)
    return f"current age mean: {current_age_mean}, future age mean: {future_age_mean}"


print(array_summary(age))
print(array_summary(income))
print(array_summary(score))
print (compare_ages(age))