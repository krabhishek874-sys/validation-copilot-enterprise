import streamlit as st
import pandas as pd
import plotly.express as px
from servicenow_client import get_validations

def show_reports():

    st.title("📊 Validation Reports Center")

    df = get_validations()

    # KPIs
    total = len(df)
    failed = len(df[df["status"] == "Failed"])
    open_count = len(df[df["status"] == "Open"])
    critical = len(df[df["priority"] == "Critical"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total", total)
    c2.metric("Failed", failed)
    c3.metric("Open", open_count)
    c4.metric("Critical", critical)

    st.divider()

    # Status Summary
    st.subheader("Validation Status Distribution")

    fig1 = px.pie(
        df,
        names="status",
        title="Status Breakdown"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # Priority Summary
    st.subheader("Priority Distribution")

    fig2 = px.bar(
        df["priority"].value_counts().reset_index(),
        x="priority",
        y="count",
        title="Priority Breakdown"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # Aging Analysis
    st.subheader("Validation Aging Report")

    fig3 = px.bar(
        df,
        x="validation_id",
        y="age",
        color="priority",
        title="Validation Aging"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # Overdue Records
    st.subheader("Overdue Validations")

    overdue = df[df["age"] > 7]

    st.dataframe(
        overdue,
        use_container_width=True
    )

    # Executive Summary
    st.subheader("Executive Summary")

    st.info(
        f"""
        Total Validations: {total}

        Failed Validations: {failed}

        Critical Validations: {critical}

        Overdue (>7 Days): {len(overdue)}
        """
    )

    # Download CSV
    st.subheader("Export Report")

    st.download_button(
        "⬇ Download Validation Report",
        df.to_csv(index=False),
        file_name="validation_report.csv",
        mime="text/csv"
    )
