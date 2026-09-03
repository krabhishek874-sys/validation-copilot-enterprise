import streamlit as st
from servicenow_client import get_validations

def show_validations():

    st.title("Validations")

    df = get_validations()

    st.write("Records loaded:", len(df))

    st.dataframe(df)
