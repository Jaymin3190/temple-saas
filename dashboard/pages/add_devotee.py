import streamlit as st

def render_add_devotee():

    st.title("➕ Add Devotee")

    with st.form("add_devotee"):

        lpm = st.text_input("LPM No")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        birthday = st.text_input("Birthday")
        address = st.text_area("Address")

        submit = st.form_submit_button("Save")

        if submit:
            st.success("Devotee added successfully")
