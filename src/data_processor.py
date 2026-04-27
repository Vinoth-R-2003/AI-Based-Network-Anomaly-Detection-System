import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def generate_synthetic_data(output_path, num_samples=1000):
    """Generates synthetic network traffic data."""
    np.random.seed(42)
    
    # Features
    duration = np.random.uniform(0, 10, num_samples)
    src_bytes = np.random.uniform(100, 5000, num_samples)
    dst_bytes = np.random.uniform(100, 5000, num_samples)
    protocol_type = np.random.choice(['TCP', 'UDP', 'ICMP'], num_samples)
    
    df = pd.DataFrame({
        'duration': duration,
        'src_bytes': src_bytes,
        'dst_bytes': dst_bytes,
        'protocol_type': protocol_type
    })
    
    # Introduce anomalies (5%)
    num_anomalies = int(0.05 * num_samples)
    anomaly_indices = np.random.choice(num_samples, num_anomalies, replace=False)
    
    # Spiking values for anomalies
    df.loc[anomaly_indices, 'duration'] *= 10
    df.loc[anomaly_indices, 'src_bytes'] *= 20
    df.loc[anomaly_indices, 'dst_bytes'] *= 20
    
    df.to_csv(output_path, index=False)
    print(f"Synthetic dataset created at {output_path}")
    return df

def preprocess_data(df):
    """Handles missing values, normalization, and encoding."""
    # Handle missing values (if any)
    df = df.fillna(df.median(numeric_only=True))
    
    # Encode categorical features
    le = LabelEncoder()
    df['protocol_type'] = le.fit_transform(df['protocol_type'])
    
    # Normalize numerical features
    scaler = StandardScaler()
    features = ['duration', 'src_bytes', 'dst_bytes', 'protocol_type']
    df[features] = scaler.fit_transform(df[features])
    
    return df, scaler, le
