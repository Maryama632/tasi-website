import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Contact Us", layout="wide")

def content():
    creators = [
        {"name": "Maryam Almousa", "linkedin": "https://www.linkedin.com/in/maryam-almousa-935053110/", "github": "https://github.com/Maryam632"},
        {"name": "Renad Alharbi", "linkedin": "http://www.linkedin.com/in/renad-alharbi7", "github": "https://github.com/renadalharbi-m"},
        {"name": "Lena Amoallim", "linkedin": "https://www.linkedin.com/in/lena-almoallim-216573273/", "github": "https://github.com/zeroallday"},
        {"name": "Bodoor Alshehri", "linkedin": "https://www.linkedin.com/", "github": "https://github.com/"}
    ]

    # ✅ Load local logo and encode it as Base64
    logo_path = Path("Tlogo.png")
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            logo_data = base64.b64encode(f.read()).decode()
        logo_src = f"data:image/png;base64,{logo_data}"
    else:
        st.warning("⚠️ Logo file not found at path: Tlogo.png")
        logo_src = ""

    # 🧭 Page Style and Navbar
    st.markdown(
        f"""
        <style>
        body {{
            background-color: #F5F7FA;
        }}

        /* Navbar */
        .navbar {{
            background-color: #1E3A8A;
            padding: 8px 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}
        .navbar .logo-container {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .navbar img {{
            height: 35px;
        }}
        .navbar .brand-name {{
            color: white;
            font-size: 22px;
            font-weight: 800;
        }}
        .navbar-links {{
            display: flex;
            gap: 20px;
        }}
        .navbar-links a {{
            color: #ffffff;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
        }}
        .navbar-links a:hover {{
            color: #FFD700;
        }}

        /* Hero */
        .hero {{
            padding: 60px 40px;
            background-color: #F5F7FA;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }}
        .hero h2 {{
            font-size: 36px;
            color: #1E3A8A;
            margin-bottom: 10px;
            font-weight: 800;
        }}
        .hero p {{
            font-size: 16px;
            color: #111827;
            max-width: 800px;
        }}

        /* Creators Section */
        .creators-section {{
            padding: 30px 40px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin: 20px 0;
        }}
        .creator-card {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #e5e7eb;
        }}
        .creator-card:last-child {{
            border-bottom: none;
        }}
        .creator-name {{
            font-size: 18px;
            font-weight: 600;
            color: #1E3A8A;
        }}
        .icons a img {{
            height: 24px;
            width: 24px;
            margin-left: 15px;
            vertical-align: middle;
        }}
        </style>

        <!-- Navbar -->
        <div class="navbar">
            <div class="logo-container">
                <img src="{logo_src}" alt="logo">
                <span class="brand-name">PrediX</span>
            </div>
            <div class="navbar-links">
                <a href="#">Home</a>
                <a href="#">TASI Vision</a>
                <a href="#">Company Insight</a>
                <a href="#">Contact Us</a>
            </div>
        </div>

        <!-- Hero Section -->
        <div class="hero">
            <h2>📞 Contact Us</h2>
            <p>Get in touch with the creators behind PrediX. Follow us on LinkedIn or check out our work on GitHub.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 👩‍💻 Creators Section
    st.markdown('<div class="creators-section"><h3>👩‍💻 Creators</h3>', unsafe_allow_html=True)

    linkedin_icon = "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg"
    github_icon = "https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg"

    for creator in creators:
        st.markdown(
            f"""
            <div class="creator-card">
                <div class="creator-name">{creator['name']}</div>
                <div class="icons">
                    <a href="{creator['linkedin']}" target="_blank">
                        <img src="{linkedin_icon}" alt="LinkedIn">
                    </a>
                    <a href="{creator['github']}" target="_blank">
                        <img src="{github_icon}" alt="GitHub">
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


# Run the page
if __name__ == "__main__":
    content()
