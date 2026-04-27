import os
import pandas as pd
from src.data_processor import generate_synthetic_data, preprocess_data
from src.model_trainer import train_isolation_forest, save_model
from src.detector import apply_detection_to_dataset
from src.visualizer import plot_anomalies

def main():
    # Paths
    DATA_PATH = os.path.join('data', 'network_traffic.csv')
    MODEL_PATH = os.path.join('models', 'isolation_forest_model.joblib')
    
    print("--- AI-Based Network Anomaly Detection System ---")
    
    # 1. Dataset Generation/Loading
    if not os.path.exists(DATA_PATH):
        print("Dataset not found. Generating synthetic data...")
        df_raw = generate_synthetic_data(DATA_PATH)
    else:
        print(f"Loading existing dataset from {DATA_PATH}...")
        df_raw = pd.read_csv(DATA_PATH)
    
    # 2. Data Processing
    print("Processing data...")
    df_processed, scaler, encoder = preprocess_data(df_raw.copy())
    
    # 3. Model Training
    print("Training Isolation Forest model...")
    model = train_isolation_forest(df_processed)
    save_model(model, MODEL_PATH)
    
    # 4. Detection
    print("Detecting anomalies...")
    df_with_anomalies = apply_detection_to_dataset(model, df_processed)
    
    # Map anomalies back to raw data for readability if needed, 
    # but here we just add the column to a copy of the raw data
    df_raw['anomaly'] = df_with_anomalies['anomaly']
    
    # 5. Output Results
    num_anomalies = (df_raw['anomaly'] == -1).sum()
    print(f"\nDetection Summary:")
    print(f"Total samples: {len(df_raw)}")
    print(f"Anomalies detected: {num_anomalies}")
    print(f"Normal traffic: {len(df_raw) - num_anomalies}")
    
    # 6. Visualization
    print("\nGenerating visualization...")
    # Use normalized data for consistent scale in plot, or raw data for better context
    # Let's use the raw data but the labels from detection
    plot_anomalies(df_raw)
    
    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    main()
