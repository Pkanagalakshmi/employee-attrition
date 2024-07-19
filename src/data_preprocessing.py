import pandas as pd

def load_data():
    data_path = 'C:\\Users\\kanag\\employee-attrition\\data\\WA_Fn-UseC_-HR-Employee-Attrition.csv'

    return pd.read_csv(data_path)

def preprocess_data(df):
    # Example preprocessing steps
    df = df.dropna()
    df = pd.get_dummies(df, drop_first=True)
    return df
