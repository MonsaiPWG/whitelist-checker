import streamlit as st
import pandas as pd
import os

# Function to load the whitelist from storage
@st.cache_data
def load_whitelist():
    file_path = "WL.xlsx"

    # Check if the file already exists
    if os.path.exists(file_path):
        df = pd.read_excel(file_path, sheet_name="Sheet1", usecols=[2], skiprows=1)
        df.columns = ["Wallet Address"]
        return set(df["Wallet Address"].dropna())
    else:
        return set()  # Return an empty set if no file exists

# Streamlit UI
st.title("🔍 PRIMOS Whitelist Checker")

# File uploader (only if WL.xlsx is missing)
if not os.path.exists("WL.xlsx"):
    uploaded_file = st.file_uploader("Upload WL.xlsx to Store Permanently", type=["xlsx"])

    if uploaded_file is not None:
        with open("WL.xlsx", "wb") as f:
            f.write(uploaded_file.getbuffer())  # Save file permanently
        st.success("✅ File uploaded and saved!")

# Load whitelist automatically
whitelist = load_whitelist()

# User input field
wallet_address = st.text_input("🔑 Wallet Address", "")

# Check whitelist status
if wallet_address:
    if wallet_address in whitelist:
        st.success("✅ Your wallet is **whitelisted**! 🎉")
    else:
        st.error("❌ Your wallet is **not whitelisted**.")

# Footer
st.markdown("---")
st.markdown("🔒 This tool only checks wallet addresses.")
