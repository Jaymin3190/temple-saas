import streamlit as st
import pandas as pd

def render_birthday_dashboard():

    st.title("🎂 Birthday Dashboard")

    data = {
        "LPM No": [101,102],
        "Name": ["Ramesh","Suresh"],
        "Phone": ["919999999999","918888888888"],
        "Birthday": ["15-05","18-06"],
        "Last Sent Date": ["","2026-05-15"]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
