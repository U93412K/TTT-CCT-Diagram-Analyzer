import pandas as pd

def load_cct_data(path):
    return pd.read_csv(path)

def basic_summary(data):
    return {
        "points": len(data),
        "min_temperature": data["temperature"].min(),
        "max_temperature": data["temperature"].max(),
    }
