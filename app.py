import streamlit as st
from modules.enzyme import enzyme_lab

st.set_page_config(page_title="Enzyme Virtual Lab", layout="wide")

st.title("🧬 Enzyme Activity Virtual Lab")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Experiment", ["Enzyme Activity"])

if page == "Enzyme Activity":
    enzyme_lab()