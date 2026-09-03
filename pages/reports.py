import streamlit as st
import plotly.express as px

from servicenow_client import get_validations


def show_reports():

    st.title("📊 Validation Reports Center")

    df = get_validations()

    total = len(df)
    failed = len(df[df["status"] == "Failed"])
    open_count = len(df[df["status"] == "Open"])
    critical = len(df[df["priority"] == "Critical"])
    overdue = len(df[df["age"] > 7])

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Total", total)
    c2.metric("Failed", failed)
    c3.metric("Open", open_count)
    c4.metric("Critical", critical)
    c5.metric("Overdue", overdue)

    st.divider()

    st.subheader("Status Distribution")

    fig1 = px.pie(
        df,
        names="status"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("Priority Distribution")

    priority_df = (
        df["priority"]
        .value_counts()
        .reset_index()
    )

    priority_df.columns = [
        "Priority",
        "Count"
    ]

    fig2 = px.bar(
        priority_df,
        x="Priority",
        y="Count",
        color="Priority"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("Validation Aging")

    fig3 = px.bar(
        df,
        x="validation_id",
        y="age",
        color="priority"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader("Overdue Validations")

    overdue_df = df[df["age"] > 7]

    st.dataframe(
        overdue_df,
        use_container_width=True
    )

    st.subheader("AI Insights")

    st.success(
        f"""
Total validations: {total}

Failed validations: {failed}

Critical validations: {critical}

Overdue validations: {overdue}

Recommended action:
Focus on Critical validations that are older than 7 days.
"""
    )

    st.subheader("Export Report")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="validation_report.csv",
        mime="text/csv"
    )
