import matplotlib.pyplot as plt
import seaborn as sns

def plot_anomalies(df, x_feature='src_bytes', y_feature='dst_bytes'):
    """Plots the network traffic, highlighting anomalies."""
    plt.figure(figsize=(10, 6))
    
    # Separate normal and anomalies
    normal = df[df['anomaly'] == 1]
    anomalies = df[df['anomaly'] == -1]
    
    sns.scatterplot(data=normal, x=x_feature, y=y_feature, color='blue', label='Normal', alpha=0.6)
    sns.scatterplot(data=anomalies, x=x_feature, y=y_feature, color='red', label='Anomaly', marker='X', s=100)
    
    plt.title('Network Traffic Anomaly Detection')
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save the plot
    plt.savefig('anomaly_plot.png')
    print("Visualization saved as anomaly_plot.png")
    plt.show()
