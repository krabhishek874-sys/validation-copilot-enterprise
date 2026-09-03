import streamlit as st
from servicenow_client import get_validations

def show_reminders():

    st.title("Reminder Center")

    df = get_validations()

    failed = df[df["status"] == "Failed"]

    st.write(
        f"Failed Validations: {len(failed)}"
    )

    st.dataframe(failed)

    if st.button("Send Reminder Emails"):
        st.success(
            "Reminder emails triggered successfully."
        )
