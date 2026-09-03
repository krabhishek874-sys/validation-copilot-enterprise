import streamlit as st

from theme import apply_theme

from pages.dashboard import show_dashboard
from pages.validations import show_validations
from pages.reminders import show_reminders
from pages.reports import show_reports

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Validation Copilot Enterprise",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# APPLY THEME
# ==========================================

apply_theme()

# ==========================================
# CUSTOM HEADER
# ==========================================

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg,#C00000,#8B0000);
        padding:15px;
        border-radius:10px;
        margin-bottom:20px;
    ">
        <h1 style="
            color:white;
            text-align:center;
            margin:0;
        ">
            📦 Validation Copilot Enterprise
        </h1>
        <p style="
            color:white;
            text-align:center;
            margin:5px;
        ">
            Validation Monitoring, Reminders & Reporting Platform
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "https://img.icons8.com/color/96/dashboard-layout.png",
    width=80
)

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "",
    [
        "Dashboard",
        "Validations",
        "Reminders",
        "Reports"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
Validation Copilot Enterprise

✅ Validation Tracking

✅ Reminder Management

✅ Aging Analysis

✅ Executive Reporting

✅ Risk Monitoring
"""
)

# ==========================================
# PAGE ROUTING
# ==========================================

if menu == "Dashboard":
    show_dashboard()

elif menu == "Validations":
    show_validations()

elif menu == "Reminders":
    show_reminders()

elif menu == "Reports":
    show_reports()

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:gray'>
        Validation Copilot Enterprise © 2026
    </div>
    """,
    unsafe_allow_html=True
)
