import streamlit as st
import requests

API_KEY = "32ea1607241a3272315569c9e81f5dc7"

if st.button("Test"):
    url = f"https://api.themoviedb.org/3/movie/550?api_key={API_KEY}&language=en-US"

    r = requests.get(url)

    st.write(r.status_code)
    st.write(r.json()["title"])