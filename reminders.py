import streamlit as st

from servicenow_client import get_validations
from notifications import send_email


def show_reminders():

    st.title("Reminder Center")

    df = get_validations()

    failed_df = df[
        df["status"] == "Failed"
    ]

    st.metric(
        "Pending Reminders",
        len(failed_df)
    )

    st.dataframe(
        failed_df,
        use_container_width=True
    )

    if st.button("Send All Reminders"):

        success = 0

        for _, row in failed_df.iterrows():

            subject = (
                f"Validation Reminder - "
                f"{row['validation_id']}"
            )

            body = f"""
            <html>
            <body>

            <h3>Validation Reminder</h3>

            <p>Hello {row['assigned_to']},</p>

            <p>
            The following validation requires attention:
            </p>

            <ul>
                <li>ID: {row['validation_id']}</li>
                <li>Description: {row['description']}</li>
                <li>Status: {row['status']}</li>
                <li>Priority: {row['priority']}</li>
                <li>Age: {row['age']} Days</li>
            </ul>

            <p>
            Please review and update the validation.
            </p>

            </body>
            </html>
            """

            if send_email(
                row["email"],
                subject,
                body
            ):
                success += 1

        st.success(
            f"{success} reminder emails sent."
        )
