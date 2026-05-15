import streamlit as st
from pages.birthday_dashboard import render_birthday_dashboard
from pages.devotee_directory import render_devotee_directory
from pages.add_devotee import render_add_devotee

st.set_page_config(
    page_title="Temple SaaS",
    layout="wide"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Birthday Dashboard",
        "Add Devotee",
        "Devotee Directory"
    ]
)

if menu == "Birthday Dashboard":
    render_birthday_dashboard()

elif menu == "Add Devotee":
    render_add_devotee()

elif menu == "Devotee Directory":
    render_devotee_directory()
