# 🛡️ AI-Based Network Anomaly Detection System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Isolation%20Forest-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An advanced machine learning solution designed to detect abnormal patterns in network traffic, providing a critical layer of defense against cybersecurity threats such as DDoS attacks, intrusions, and data exfiltration.

---

## 🚀 Overview

This system leverages the **Isolation Forest** algorithm to identify deviations from "normal" network behavior. Unlike traditional rule-based systems, this AI-driven approach can detect "Zero-Day" attacks by learning the baseline characteristics of your network traffic and flagging outliers that exhibit suspicious patterns.

### 🔍 Key Features
- **Real-time Detection Logic**: Implements `detect_anomaly(input_data)` for immediate classification.
- **Automated Preprocessing**: Handles missing values, normalization, and categorical encoding (`LabelEncoding`).
- **Synthetic Traffic Generator**: Built-in capability to generate realistic network datasets for testing and benchmarking.
- **Dynamic Visualization**: Automatically generates scatter plots to visually distinguish between normal traffic and anomalies.
- **Model Persistence**: Saves trained models for future inference without retraining.

---

## 🛠️ Technology Stack
- **Core Logic**: Python 3.x
- **Data Handling**: `Pandas`, `NumPy`
- **Machine Learning**: `Scikit-Learn` (Isolation Forest)
- **Visualization**: `Matplotlib`, `Seaborn`
- **Persistence**: `Joblib`

---

## 📁 Project Structure
```text
/
├── data/               # Raw and processed network datasets
├── models/             # Serialized trained models (.joblib)
├── src/                # Modular source code
│   ├── data_processor.py   # Data cleaning and generation
│   ├── model_trainer.py    # Training logic
│   ├── detector.py         # Inference and classification
│   └── visualizer.py       # Matplotlib plotting logic
├── main.py             # Pipeline entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/network-anomaly-detection.git
   cd network-anomaly-detection
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the detection pipeline**:
   ```bash
   python main.py
   ```

---

## 📊 Sample Output
When you run the system, it processes 1,000 traffic samples and identifies anomalies based on features like `duration`, `src_bytes`, and `dst_bytes`.

**Console Output:**
```text
Detection Summary:
Total samples: 1000
Anomalies detected: 50
Normal traffic: 950
```

**Visualization Result:**
An `anomaly_plot.png` is generated, highlighting anomalies in **Red (X)** and normal traffic in **Blue**.

---

## 🛡️ Cybersecurity Context
Anomaly detection is the cornerstone of modern **Intrusion Detection Systems (IDS)**. By monitoring traffic metrics, this system can identify:
- **DDoS Attacks**: Sudden, massive spikes in bytes sent/received.
- **Port Scanning**: Unusual duration and frequency of connections.
- **Exfiltration**: Abnormal destination byte counts indicating data theft.

---

## 🤝 Contributing
Contributions are welcome! If you have ideas for improving the detection accuracy (e.g., using Autoencoders or LSTMs), feel free to open a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
