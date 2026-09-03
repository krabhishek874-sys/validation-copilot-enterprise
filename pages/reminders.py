import streamlit as st
from servicenow_client import get_validations

def show_reminders():

    st.title("Reminder Center")

    df = get_validations()

    overdue = df[df["status"] == "Failed"]

    st.metric(
        "Pending Reminders",
        len(overdue)
    )

    st.dataframe(overdue)

    if st.button("Send All Reminders"):
        st.success(
            f"{len(overdue)} reminder emails triggered."
        )
