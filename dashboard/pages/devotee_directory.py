import streamlit as st
import pandas as pd

def render_devotee_directory():

    st.title("🗄️ Devotee Directory")

    data = {
        "LPM No": [101,102],
        "Name": ["Ramesh","Suresh"],
        "Phone": ["919999999999","918888888888"],
        "Birthday": ["15-05","18-06"],
        "Address": ["Jamnagar","Rajkot"]
    }

    df = pd.DataFrame(data)

    st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic"
    )
