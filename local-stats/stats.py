import numpy as np
from scipy import stats


def get_stats(arr):
    """
    Returns a string containing the mean, median, mode, and standard deviation of an array
    """
    mean = np.mean(arr)
    median = np.median(arr)
    mode = stats.mode(arr, keepdims=False)
    sd = np.std(arr)
    return f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {sd:.2f}"


arr = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
print(get_stats(arr))