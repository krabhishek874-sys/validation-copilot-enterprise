# servicenow_client.py

import pandas as pd

def get_validations():
    return pd.read_csv("data/validations.csv")
