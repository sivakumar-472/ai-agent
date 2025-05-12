import streamlit as st
import requests

# Set Streamlit page config
st.set_page_config(page_title="Morning Market Brief", page_icon="🧠")

# App Title
st.title("🧠 Morning Market Brief Assistant")

# Instruction
st.write("Click the button below to generate today's market brief:")

# Button
if st.button("Generate Brief"):
    try:
        # Make POST request to backend API
        response = requests.post("http://localhost:8006/api/brief")

        # Check response status
        if response.status_code == 200:
            data = response.json()
            brief = data.get("narrative", "No narrative returned.")
            st.success(brief)
        else:
            st.error(f"Failed to fetch data from backend. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend API: {e}")
