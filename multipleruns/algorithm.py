def main(data, function):
    """Take the average along the long axis with the specified function"""
    return {
        "result": getattr(data, function)(axis=1).to_frame(name="result"),
    }
