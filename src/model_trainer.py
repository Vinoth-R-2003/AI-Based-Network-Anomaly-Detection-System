from sklearn.ensemble import IsolationForest
import joblib
import os

def train_isolation_forest(df, contamination=0.05):
    """Trains an Isolation Forest model on the provided dataframe."""
    # Isolation Forest doesn't need 'y' labels for training
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(df)
    return model

def save_model(model, path):
    """Saves the trained model to the specified path."""
    joblib.dump(model, path)
    print(f"Model saved to {path}")

def load_model(path):
    """Loads a model from the specified path."""
    if os.path.exists(path):
        return joblib.load(path)
    else:
        raise FileNotFoundError(f"No model found at {path}")
