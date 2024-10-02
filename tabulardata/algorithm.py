def main(data):
    """Take the mean of a time series along the time axis"""
    return {
        "mean": data.mean(axis=1).to_frame(name="mean"),
    }
