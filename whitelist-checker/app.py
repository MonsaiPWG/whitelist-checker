import streamlit as st
import pandas as pd

# Function to load the whitelist from the Excel file
@st.cache_data
def load_whitelist():
    uploaded_file = st.file_uploader("Upload Whitelist File (WL.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Sheet1", usecols=[2], skiprows=1)
    df.columns = ["Wallet Address"]
    whitelist = set(df["Wallet Address"].dropna())
else:
    st.warning("⚠ Please upload WL.xlsx to check addresses.")
    whitelist = set()  # Ensure this file is in the same directory
    df = pd.read_excel(file_path, sheet_name="Sheet1", usecols=[2], skiprows=1)
    df.columns = ["Wallet Address"]
    return set(df["Wallet Address"].dropna())  # Convert to a set for fast lookup

# Load the whitelist
whitelist = load_whitelist()

# Streamlit UI
st.title("🔍 Whitelist Checker")
st.write("Enter your wallet address below to check if you're whitelisted.")

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
st.markdown("🔒 This tool only checks wallet addresses. Editing the whitelist is not allowed.")

# Refresh button (optional)
if st.button("🔄 Refresh Whitelist"):
    whitelist = load_whitelist()
    st.success("Whitelist reloaded successfully!")
