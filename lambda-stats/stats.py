import numpy as np
from scipy import stats


def lambda_handler(event, context):
    def get_stats(arr):
        """
        Returns a string containing the mean, median, mode, and standard deviation of an array
        """
        mean = np.mean(arr)
        median = np.median(arr)
        mode = stats.mode(arr, keepdims=False)
        sd = np.std(arr)
        return f"Mean: {mean}, Median: {median}, Mode: {mode}, Standard Deviation: {sd:.2f}"

    stat_str = get_stats(event["array"])

    return {
        "statusCode": 200,
        "body": stat_str
    }