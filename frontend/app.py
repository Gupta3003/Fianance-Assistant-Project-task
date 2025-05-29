import streamlit as st
import requests

st.title("🧠 Market Finance Assistant")

symbol = st.text_input("Enter Stock Symbol:")

if st.button("Get Market Brief"):
    try:
        response = requests.get(f"http://localhost:8004/orchestrate/{symbol}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                brief = data.get("brief")
                if brief:
                    st.write(brief)
                else:
                    st.warning("The response JSON does not contain 'brief'.")
            except ValueError:
                st.error("Received response is not valid JSON.")
                st.text(response.text)
        else:
            st.error(f"API returned error status code: {response.status_code}")
            st.text(response.text)
    
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

