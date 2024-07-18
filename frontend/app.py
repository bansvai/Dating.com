import streamlit as st
import pandas as pd
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

# Button to fetch random user and nearest users
st.header("Fetch Random User and Nearest Users")
if st.button("Fetch Random User and Nearest Users"):
    response = requests.get(f"{API_URL}/random_user_and_nearest_users")
    if response.status_code == 200:
        data = response.json()
        random_user = data["random_user"]
        nearest_users = data["nearest_users"]

        # Displaying random user details
        st.subheader("Random User")
        st.write(f"Name: {random_user['first_name']} {random_user['last_name']}")
        st.write(f"Email: {random_user['email']}")
        st.write(f"Coordinates: ({random_user['latitude']}, {random_user['longitude']})")

        map_data = pd.DataFrame(nearest_users)

        st.subheader("Nearest Users on Map")
        st.map(map_data[['latitude', 'longitude']])
    elif response.status_code == 404:
        st.error("No user found.")
    else:
        st.error("Failed to fetch users.")