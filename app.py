import streamlit as st

from pages.dashboard import show_dashboard
from pages.validations import show_validations
from pages.reminders import show_reminders
from pages.reports import show_reports


st.set_page_config(
    page_title="Validation Copilot Enterprise",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📦 Validation Copilot")

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Validations",
        "Reminders",
        "Reports"
    ]
)

if menu == "Dashboard":
    show_dashboard()

elif menu == "Validations":
    show_validations()

elif menu == "Reminders":
    show_reminders()

elif menu == "Reports":
    show_reports()

