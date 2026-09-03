import streamlit as st


def apply_theme():

    st.markdown("""
    <style>

    /* ====================================================
       MAIN APPLICATION BACKGROUND
    ==================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #fff5f5 35%,
            #ffeaea 70%,
            #ffffff 100%
        );
    }

    /* ====================================================
       SIDEBAR
    ==================================================== */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #c00000 0%,
            #8b0000 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Hide Streamlit automatic page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* ====================================================
       TITLES
    ==================================================== */

    h1 {
        color: #b30000 !important;
        font-weight: 700;
    }

    h2 {
        color: #b30000 !important;
        font-weight: 600;
    }

    h3 {
        color: #b30000 !important;
    }

    /* ====================================================
       KPI METRIC CARDS
    ==================================================== */

    div[data-testid="stMetric"] {

        background-color: white;

        padding: 20px;

        border-radius: 15px;

        border-left: 6px solid #c00000;

        box-shadow:
            0 4px 15px rgba(0,0,0,0.12);

        text-align: center;
    }

    /* ====================================================
       BUTTONS
    ==================================================== */

    .stButton button {

        background-color: #c00000 !important;

        color: white !important;

        border-radius: 10px;

        border: none;

        font-weight: bold;

        width: 100%;
    }

    .stButton button:hover {

        background-color: #8b0000 !important;

        color: white !important;
    }

    /* ====================================================
       DOWNLOAD BUTTON
    ==================================================== */

    .stDownloadButton button {

        background-color: #c00000 !important;

        color: white !important;

        border-radius: 10px;

        border: none;
    }

    /* ====================================================
       DATA TABLES
    ==================================================== */

    .stDataFrame {

        background-color: white;

        border-radius: 12px;

        padding: 10px;

        box-shadow:
            0 4px 10px rgba(0,0,0,0.08);
    }

    /* ====================================================
       INPUT FIELDS
    ==================================================== */

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div {

        background-color: white;

        border-radius: 8px;
    }

    /* ====================================================
       SUCCESS BOXES
    ==================================================== */

    .stSuccess {

        border-left: 5px solid #c00000;
    }

    /* ====================================================
       INFO BOXES
    ==================================================== */

    .stInfo {

        border-left: 5px solid #c00000;
    }

    /* ====================================================
       EXPANDERS
    ==================================================== */

    .streamlit-expanderHeader {

        color: #b30000 !important;

        font-weight: bold;
    }

    /* ====================================================
       SCROLLBAR
    ==================================================== */

    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: #c00000;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f5f5f5;
    }

    </style>
    """, unsafe_allow_html=True)
