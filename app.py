import streamlit as st

from modules.dashboard import birthday_dashboard
from modules.devotees import devotee_crud
from modules.automation import run_automation

st.set_page_config(
    page_title="Temple SaaS",
    layout="wide",
    page_icon="🎂"
)

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
.block-container {
    padding-top: 1rem;
}
.stButton > button {
    border-radius: 8px;
    border: none;
    background: #2563eb;
    color: white;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛕 Temple SaaS")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🎂 Birthday Dashboard",
        "👥 Devotee Directory",
        "🤖 WhatsApp Automation"
    ]
)

if menu == "🎂 Birthday Dashboard":
    birthday_dashboard()

elif menu == "👥 Devotee Directory":
    devotee_crud()

elif menu == "🤖 WhatsApp Automation":
    run_automation()
