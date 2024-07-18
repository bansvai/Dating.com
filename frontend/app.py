import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000"

st.title("Dating.com 💘")

# Scrape Random Users
st.header("Scrape Random Users")
num_users = st.number_input("Number of users to scrape", value=150)
if st.button("Scrape Users"):
    if num_users < 101:
        st.error("Number of users must be greater than 100.")
        st.stop()
    if num_users > 500:
        st.error("Number of users can't be greater than 500.")
        st.stop()
    response = requests.post(f"{API_URL}/scrape_users", json={"num_users": num_users})
    if response.status_code == 200:
        st.success(f"Successfully scraped {num_users} users.")
    else:
        st.error("Failed to scrape users.")