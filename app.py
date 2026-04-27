import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from src.data_processor import generate_synthetic_data, preprocess_data
from src.model_trainer import train_isolation_forest, save_model
from src.detector import apply_detection_to_dataset

# Page Configuration
st.set_page_config(
    page_title="AI Network Anomaly Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    
    /* Header Styling */
    .main-header {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 3rem;
        background: -webkit-linear-gradient(#00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Glassmorphism Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #00d2ff;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background-color: rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Custom Button */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.5);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Helper Functions
def run_pipeline(df_raw):
    df_processed, scaler, encoder = preprocess_data(df_raw.copy())
    model = train_isolation_forest(df_processed)
    df_with_anomalies = apply_detection_to_dataset(model, df_processed)
    df_raw['anomaly'] = df_with_anomalies['anomaly']
    return df_raw

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.title("Settings")
    st.markdown("---")
    
    data_source = st.radio("Data Source", ["Generate Synthetic", "Upload CSV"])
    
    if data_source == "Generate Synthetic":
        num_samples = st.slider("Number of Samples", 100, 5000, 1000)
        if st.button("Generate & Process"):
            with st.spinner("Simulating network traffic..."):
                DATA_PATH = os.path.join('data', 'network_traffic.csv')
                df_raw = generate_synthetic_data(DATA_PATH, num_samples=num_samples)
                st.session_state['df'] = run_pipeline(df_raw)
                st.success("Data Generated!")
    
    else:
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df_raw = pd.read_csv(uploaded_file)
            if st.button("Process Data"):
                with st.spinner("Analyzing traffic..."):
                    st.session_state['df'] = run_pipeline(df_raw)
                    st.success("Analysis Complete!")

# --- Main Dashboard ---
st.markdown('<p class="main-header">🛡️ Network Security Dashboard</p>', unsafe_allow_html=True)
st.markdown("##### Real-time AI Anomaly Detection System")

if 'df' in st.session_state:
    df = st.session_state['df']
    num_anomalies = (df['anomaly'] == -1).sum()
    total = len(df)
    anomaly_pct = (num_anomalies / total) * 100

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>Total Packets</h3><h2>{total}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3 style="color:#ff4b4b">Anomalies</h3><h2>{num_anomalies}</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h3>Anomaly Rate</h3><h2>{anomaly_pct:.1f}%</h2></div>', unsafe_allow_html=True)
    with col4:
        health_color = "#00ff00" if anomaly_pct < 10 else "#ffcc00"
        st.markdown(f'<div class="metric-card"><h3>System Health</h3><h2 style="color:{health_color}">{"SECURE" if anomaly_pct < 10 else "WARNING"}</h2></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Visualization and Data
    tab1, tab2 = st.tabs(["📊 Interactive Analysis", "📄 Detection Logs"])
    
    with tab1:
        st.subheader("Traffic Analysis Visualization")
        # Plotly Scatter
        fig = px.scatter(
            df, 
            x='src_bytes', 
            y='dst_bytes', 
            color=df['anomaly'].map({1: 'Normal', -1: 'Anomaly'}),
            color_discrete_map={'Normal': '#00d2ff', 'Anomaly': '#ff4b4b'},
            symbol=df['anomaly'].map({1: 'circle', -1: 'x'}),
            hover_data=['duration', 'protocol_type'],
            template="plotly_dark"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_title="Source Bytes",
            yaxis_title="Destination Bytes",
            font=dict(family="Inter, sans-serif", size=12)
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Suspicious Activity Logs")
        anomalies_df = df[df['anomaly'] == -1].tail(20)
        st.dataframe(anomalies_df.style.background_gradient(subset=['src_bytes', 'dst_bytes'], cmap='Reds'), use_container_width=True)

else:
    # Landing Page State
    st.info("👋 Welcome! Please generate synthetic data or upload a CSV from the sidebar to begin the analysis.")
    
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070", caption="AI-Driven Security Monitoring")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### How it works
        1. **Baseline Learning**: The system analyzes normal traffic patterns.
        2. **Isolation Forest**: Using unsupervised ML, it isolates "outliers" that deviate from the norm.
        3. **Real-time Alerting**: Potential DDoS or intrusion attempts are flagged immediately.
        """)
    with col2:
        st.markdown("""
        ### Why AI?
        Traditional firewalls use fixed rules. Our AI learns and adapts, identifying **Zero-Day** threats that have never been seen before.
        """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.5);'>Built with ❤️ for Network Security Professionals</p>", unsafe_allow_html=True)
