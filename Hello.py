# pages/home.py
# ==================================
# PrediX - Home Page (Minimal Design)
# ==================================

import streamlit as st

st.set_page_config(page_title="PrediX - Home", layout="wide")

# 🪄 تنسيق مدمج (Navbar + Hero Section)
st.markdown(
    """
    <style>
    :root {
        --brand-blue: #1E3A8A;
        --brand-light-blue: #2563EB;
        --background: #F8FAFC;
        --text-color: #0F172A;
        --muted-text: #475569;
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

    /* 🧭 Hero Section */
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

    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 15px;
        }
        .hero {
            text-align: center;
            padding: 60px 15px;
        }
        .hero h1 {
            font-size: 36px;
        }
        .hero p {
            font-size: 18px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# 🧭 NAVBAR
# ============================


st.markdown(
    """
    <div class="navbar">
    <div class="logo">
        <img src="https://github.com/Maryama632/TASI_vision/blob/master/Tlogo.png" alt="logo">
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

# ============================
# 🧭 HERO SECTION
# ============================
st.markdown(
    """
    <div class="hero">
        <h1>Saudi Stock Market<br>Smart Insights</h1>
        <p>
            Innovative platform that provides reliable forecasts for the Saudi stock market,
            helping investors make smarter, data-driven decisions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


def content():
    st.header("Home")
