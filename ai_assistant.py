import streamlit as st

def show_ai():

    st.title("AI Assistant")

    question = st.text_input(
        "Ask a question about validations"
    )

    if question:

        st.info(
            "Azure OpenAI integration will answer questions here."
        )

        st.write(
            f"Question: {question}"
        )
