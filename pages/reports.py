import streamlit as st
import pandas as pd
import plotly.express as px

from servicenow_client import get_validations


def show_reports():

    st.title("📊 Validation Reports Center")

    df = get_validations()

    # ==========================
    # KPI SECTION
    # ==========================

    total = len(df)

    failed = len(
        df[df["status"] == "Failed"]
    )

    open_count = len(
        df[df["status"] == "Open"]
    )

    critical = len(
        df[df["priority"] == "Critical"]
    )

    overdue = len(
        df[df["age"] > 7]
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Total", total)
    c2.metric("Failed", failed)
    c3.metric("Open", open_count)
    c4.metric("Critical", critical)
    c5.metric("Overdue", overdue)

    st.divider()

    # ==========================
    # STATUS DISTRIBUTION
    # ==========================

    st.subheader("📈 Validation Status Distribution")

    status_chart = px.pie(
        df,
        names="status",
        title="Validation Status Breakdown"
    )

    st.plotly_chart(
        status_chart,
        use_container_width=True
    )

    # ==========================
    # PRIORITY BREAKDOWN
    # ==========================

    st.
