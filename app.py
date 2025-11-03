import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="🏥 Medical Data Processing System", layout="wide")

# Define main app
def main():
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Login Page
    if not st.session_state.logged_in:
        st.title("🏥 Medical Data Processing System")
        st.subheader("Login")

        username = st.text_input("User Name")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "demo app" and password == "demo@123":
                st.session_state.logged_in = True
                st.success("✅ Login successful")
            else:
                st.error("❌ Invalid username or password")

    # Main Dashboard (after login)
    else:
        st.title("📊 Welcome to the Medical Data Processing System")
        st.write("You are successfully logged in as **Demo User**.")

        # Example content after login
        uploaded_file = st.file_uploader("📂 Upload your medical CSV data", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("### Preview of Uploaded Data:")
            st.dataframe(df.head())

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.success("You have been logged out successfully.")

# Run the app
if __name__ == "__main__":
    main()
