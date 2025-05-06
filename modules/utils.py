import streamlit as st
from datetime import datetime

def initialize_session():
    if "step" not in st.session_state:
        st.session_state.step = 1

def get_today_str():
    return datetime.today().strftime("%Y%m%d")
