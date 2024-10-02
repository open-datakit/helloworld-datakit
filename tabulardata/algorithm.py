def main(data):
    """Take the average of the input data along the long axis"""
    return {
        "result": data.mean(axis=1).to_frame(name="result"),
    }
