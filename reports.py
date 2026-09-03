import streamlit as st
from servicenow_client import get_validations

def show_reports():

    st.title("Reports")

    df = get_validations()

    st.download_button(
        label="Download CSV Report",
        data=df.to_csv(index=False),
        file_name="validation_report.csv",
        mime="text/csv"
    )
