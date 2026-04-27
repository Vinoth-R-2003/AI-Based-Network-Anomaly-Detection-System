import pandas as pd

def detect_anomaly(model, input_data):
    """
    Predicts if the input data is normal (1) or an anomaly (-1).
    input_data should be a preprocessed pandas DataFrame or numpy array.
    """
    prediction = model.predict(input_data)
    return prediction

def apply_detection_to_dataset(model, df):
    """Applies detection to the entire dataset and adds an 'anomaly' column."""
    df['anomaly'] = model.predict(df)
    # Isolation Forest returns 1 for inliers and -1 for outliers
    return df
