import streamlit as st
from pages.dashboard import show_dashboard
from pages.validations import show_validations
from pages.reminders import show_reminders
from pages.reports import show_reports
from pages.ai_assistant import show_ai

st.set_page_config(page_title='Validation Copilot Enterprise',layout='wide')
menu=st.sidebar.radio('Navigation',['Dashboard','Validations','Reminders','Reports','AI Assistant'])
if menu=='Dashboard': show_dashboard()
elif menu=='Validations': show_validations()
elif menu=='Reminders': show_reminders()
elif menu=='Reports': show_reports()
else: show_ai()