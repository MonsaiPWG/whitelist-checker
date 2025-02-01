import streamlit as st
import pandas as pd

# Function to load the whitelist from an uploaded file
def load_whitelist(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, sheet_name="Sheet1", usecols=[2], skiprows=1)
        df.columns = ["Wallet Address"]
        return set(df["Wallet Address"].dropna())  # Convert to a set for fast lookup
    else:
        return set()  # Return an empty set if no file is uploaded

# Streamlit UI
st.title("🔍 Whitelist Checker")
st.write("Upload your whitelist file and enter your wallet address to check if you're whitelisted.")

# File uploader for whitelist
uploaded_file = st.file_uploader("Upload Whitelist File (WL.xlsx)", type=["xlsx"])

# Load whitelist dynamically
whitelist = load_whitelist(uploaded_file)

# User input field
wallet_address = st.text_input("🔑 Wallet Address", "")

# Check whitelist status
if wallet_address:
    if whitelist and wallet_address in whitelist:
        st.success("✅ Your wallet is **whitelisted**! 🎉")
    elif whitelist:
        st.error("❌ Your wallet is **not whitelisted**.")
    else:
        st.warning("⚠ Upload WL.xlsx first to check addresses.")

# Footer
st.markdown("---")
st.markdown("🔒 This tool only checks wallet addresses. Editing the whitelist is not allowed.")



