import streamlit as st
import pandas as pd

st.set_page_config(page_title="PrediX - TASI Vision", layout="wide")

st.markdown("""
<style>
:root {
    --brand-blue: #1E3A8A;
    --brand-light-blue: #2563EB;
    --background: #F8FAFC;
    --text-color: #0F172A;
    --muted-text: #475569;
    --success: #16A34A;
    --danger: #DC2626;
    --warning: #FACC15;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--background);
    color: var(--text-color);
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
}

/* ✅ Navbar */
.navbar {
    background-color: var(--brand-blue);
    padding: 14px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    border-radius: 0 0 10px 10px;
}

.navbar .logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.navbar .logo img {
    height: 40px;
}

.navbar .logo h1 {
    color: white;
    font-size: 22px;
    font-weight: 800;
    margin: 0;
}

.navbar .links {
    display: flex;
    gap: 25px;
}

.navbar .links a {
    color: white;
    text-decoration: none;
    font-size: 16px;
    font-weight: 500;
    transition: color 0.3s ease;
}

.navbar .links a:hover {
    color: #FFD700;
}

/* 🧭 Hero */
.hero {
    padding: 90px 20px;
    text-align: left;
    max-width: 900px;
    margin: 0 auto;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    color: var(--brand-blue);
    margin-bottom: 20px;
    line-height: 1.2;
}

.hero p {
    font-size: 20px;
    color: var(--muted-text);
    line-height: 1.6;
    max-width: 700px;
}

/* 📊 Prediction Box */
.prediction-box {
    display:inline-block;
    background:white;
    padding:20px 30px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    max-width:600px;
    text-align: center;
}

.prediction-box h3 {
    color: var(--brand-blue);
    margin-bottom: 10px;
}

.prediction-box span {
    font-weight: 700;
}

@media (max-width: 768px) {
    .navbar { flex-direction: column; gap: 15px; }
    .hero { text-align: center; padding: 60px 15px; }
    .hero h1 { font-size: 36px; }
    .hero p { font-size: 18px; }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🧭 Navbar
# =========================================================
st.markdown("""
<div class="navbar">
    <div class="logo">
        <img src="https://cdn-icons-png.flaticon.com/512/684/684908.png" alt="logo">
        <h1>PrediX</h1>
    </div>
    <div class="links">
        <a href="/?page=home">Home</a>
        <a href="/?page=tasi_vision" style="color:#FFD700;">TASI Vision</a>
        <a href="/?page=insight">Company Insight</a>
        <a href="/?page=contact">Contact Us</a>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 🧭 Hero Section
# =========================================================
st.markdown("""
<div class="hero">
    <h1>TASI Vision 📈</h1>
    <p>
        TASI (Tadawul All Share Index) is the main index that measures the performance
        of all listed companies in the Saudi stock market.
        It reflects the overall market direction and investor sentiment in the Kingdom.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 Saudi Stock Market Index (TASI)")

st.image("tasi-model.webp")
st.image("tasi-60.webp")


st.markdown(
    """
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049; /* Darker green on hover */
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrapper to center it
st.markdown('<div class="centered-button">', unsafe_allow_html=True)
if st.button("Prediction"):
    st.markdown("""
    <div style="text-align:center; margin-top:40px;">
        <div class="prediction-box">
            <h3>Predicted Market Trend: <span style="color:#16A34A;">Upward 📈</span></h3>
            <p style="color:#334155;">
                Based on the latest AI forecasting model, the TASI index is expected to move upward for the next 60 days.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
