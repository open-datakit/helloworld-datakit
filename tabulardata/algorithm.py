def main(data):
    """Average a time series along the time axis"""
    return {
        "average": data.mean(axis=1).to_frame(name="average"),
    }
