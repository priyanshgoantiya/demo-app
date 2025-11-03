import streamlit as st
import pandas as pd

# --- User database ---
USERS = {
    "vinno": "xyz",
    "jupiter_user1": "priyansh"
}

# --- Initialize session state ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None


def login_page():
    """Display login page"""
    st.title("🏥 Medical Data Processing System")
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password")


def logout():
    """Logout function"""
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()


def main_app():
    """Main application after login"""
    st.title("🏥 Medical Data Processing System")
    
    with st.sidebar:
        st.write(f"Logged in as: **{st.session_state.username}**")
        if st.button('Logout'):
            logout()
        st.divider()
        st.subheader("Select data type")
        data_type = st.radio(
            "Choose your input:",
            ["Treatment Given", "Relevant Investigation", "Diagnosis", "Demographic Data"]
        )

    st.header(f"{data_type}")


def main():
    """Main entry point"""
    st.set_page_config(
        page_title="Medical Data Processing System",
        page_icon="🏥",
        layout="wide"
    )
    
    if not st.session_state.logged_in:
        login_page()
    else:
        main_app()


if __name__ == "__main__":
    main()

