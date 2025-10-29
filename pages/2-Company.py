import streamlit as st

st.set_page_config(page_title="PrediX - Company Insight" , layout="wide")

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
    padding: 90px 20px 50px 20px;
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

/* Forecast Box */
.forecast-box {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    margin-top: 25px;
}

@media (max-width: 768px) {
    .navbar { flex-direction: column; gap: 15px; }
    .hero { text-align: center; padding: 60px 15px; }
    .hero h1 { font-size: 36px; }
    .hero p { font-size: 18px; }
}
</style>
""", unsafe_allow_html=True)


COMPANIES = {
    "Aramco": {
        "ticker": "2222.SR",
        "sector": "Energy",
        "desc": "Leading global energy company",
        "image_model_name": "Imges/aramco_model.webp",
        "image_60_name": "Imges/aramco_60.webp",
        "trend": "upward"
    },
    "Al Rajhi Bank": {
        "ticker": "1120.SR",
        "sector": "Banking",
        "desc": "Largest Islamic bank worldwide",
        "image_model_name": "Imges/rajhi_model.webp",
        "image_60_name": "Imges/rajhi_60.webp",
        "trend": "upward"
    },
    "Elm": {
        "ticker": "7203.SR",
        "sector": "Technology",
        "desc": "Digital innovation and solutions",
        "image_model_name": "Imges/elm_model.webp",
        "image_60_name": "Imges/elm_60.webp",
        "trend": "downward"
    }
}

# 🧭 Navbar
import base64
from pathlib import Path

logo_path = Path("Tlogo.png")
if logo_path.exists():
    with open(logo_path, "rb") as f:
        logo_data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div class="navbar">
            <div class="logo">
                <img src="data:image/png;base64,{logo_data}" alt="logo" height="40">
                <h1>PrediX</h1>
            </div>
            <div class="links">
                <a href="/?page=home">Home</a>
                <a href="/?page=tasi_vision" style="color:#FFD700;">TASI Vision</a>
                <a href="/?page=insight">Company Insight</a>
                <a href="/?page=contact">Contact Us</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("⚠️ Logo file not found at path: Tlogo.png")

# 🧭 Hero Section
st.markdown("""
<div class="hero">
    <h1>🏢 Company Insight</h1>
    <p>
        Explore financial data, performance trends, and AI-powered forecasts
        for leading Saudi companies listed in the Tadawul exchange.
    </p>
</div>
""", unsafe_allow_html=True)

# 🏢 Company Selector
st.markdown("### 🔽 Select a Company")
selected = st.selectbox("Choose a company:", list(COMPANIES.keys()))

if selected:
    info = COMPANIES[selected]
    ticker = info["ticker"]
    sector = info["sector"]
    desc = info["desc"]
    clean_ticker = ticker.replace(".SR", "")

    # 🔹 المعلومات أولاً (فوق)
    st.markdown(f"**Company:** {selected} ({clean_ticker})")
    st.markdown(f"**Sector:** {sector}")
    st.markdown(f"**Description:** {desc}")

    # 🔹 بعدين الصور (تحت)
    st.image(info["image_model_name"])
    st.image(info["image_60_name"])

    # 🔹 تنسيق الزر
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

        if info["trend"] == "upward":
            st.markdown("""
            <div style="text-align:center; margin-top:40px;">
                <div class="prediction-box">
                    <h3>Predicted Market Trend: <span style="color:#16A34A;">Upward 📈</span></h3>
                    <p style="color:#334155;">
                        Based on the latest AI forecasting model, the Company index is expected to move upward for the next 60 days.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if info["trend"] == "downward":
                st.markdown("""
                <div style="text-align:center; margin-top:40px;">
                    <div class="prediction-box">
                        <h3>Predicted Market Trend: <span style="color:#DC2626;">Downward 📉</span></h3>
                        <p style="color:#334155;">
                            Based on the latest AI forecasting model, the company index is expected to move downward for the next 60 days.
                        </p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
