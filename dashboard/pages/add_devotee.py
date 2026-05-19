import streamlit as st
import pandas as pd
import sqlite3
import os

# =========================================================
# DATABASE PATH
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "temple.db"
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)

# =========================================================
# SQLITE CONNECTION
# =========================================================
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

# =========================================================
# CREATE TABLE
# =========================================================
conn.execute("""
CREATE TABLE IF NOT EXISTS devotees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    dob TEXT,
    photo TEXT
)
""")

conn.commit()

# =========================================================
# PAGE FUNCTION
# =========================================================
def render_add_devotee():

    st.title("➕ Add Devotee")

    # =====================================================
    # SESSION STATE
    # =====================================================
    if "edit_id" not in st.session_state:
        st.session_state.edit_id = None

    # =====================================================
    # FETCH SECTION
    # =====================================================
    st.subheader("🔍 Fetch Devotee")

    fetch_id = st.text_input("Enter Devotee ID")

    if st.button("Fetch Devotee"):

        if fetch_id:

            fetched = pd.read_sql(
                f"SELECT * FROM devotees WHERE id={fetch_id}",
                conn
            )

            if not fetched.empty:

                row = fetched.iloc[0]

                st.session_state.edit_id = row["id"]
                st.session_state.name = row["name"]
                st.session_state.address = row["address"]
                st.session_state.dob = row["dob"]
                st.session_state.photo = row["photo"]

                st.success("Devotee fetched successfully")

            else:
                st.error("No devotee found")

    st.markdown("---")

    # =====================================================
    # FORM
    # =====================================================
    with st.form("devotee_form"):

        name = st.text_input(
            "Name",
            value=st.session_state.get("name", "")
        )

        address = st.text_area(
            "Address",
            value=st.session_state.get("address", "")
        )

        dob = st.text_input(
            "Date of Birth",
            value=st.session_state.get("dob", "")
        )

        photo = st.file_uploader(
            "Upload Photo",
            type=["jpg", "jpeg", "png"]
        )

        c1, c2 = st.columns(2)

        with c1:
            save = st.form_submit_button("💾 Save")

        with c2:
            update = st.form_submit_button("✏️ Update")

    # =====================================================
    # SAVE NEW DEVOTEE
    # =====================================================
    if save:

        photo_path = ""

        if photo:

            photo_path = os.path.join(
                UPLOAD_DIR,
                photo.name
            )

            with open(photo_path, "wb") as f:
                f.write(photo.getbuffer())

        conn.execute("""
            INSERT INTO devotees (
                name,
                address,
                dob,
                photo
            )
            VALUES (?, ?, ?, ?)
        """, (
            name,
            address,
            dob,
            photo_path
        ))

        conn.commit()

        st.success("Devotee saved successfully")

        st.rerun()

    # =====================================================
    # UPDATE DEVOTEE
    # =====================================================
    if update:

        if st.session_state.edit_id is None:

            st.error("Fetch devotee first")

        else:

            photo_path = st.session_state.get(
                "photo",
                ""
            )

            if photo:

                photo_path = os.path.join(
                    UPLOAD_DIR,
                    photo.name
                )

                with open(photo_path, "wb") as f:
                    f.write(photo.getbuffer())

            conn.execute("""
                UPDATE devotees
                SET
                    name=?,
                    address=?,
                    dob=?,
                    photo=?
                WHERE id=?
            """, (
                name,
                address,
                dob,
                photo_path,
                st.session_state.edit_id
            ))

            conn.commit()

            st.success("Devotee updated successfully")

            st.rerun()

    # =====================================================
    # SHOW ALL DEVOTEES
    # =====================================================
    st.markdown("---")

    st.subheader("📋 All Devotees")

    devotees_df = pd.read_sql(
        "SELECT * FROM devotees ORDER BY id DESC",
        conn
    )

    st.dataframe(
        devotees_df,
        use_container_width=True
    )