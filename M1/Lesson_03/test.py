import time
import streamlit as st

with st.status("Loading...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(3)
    st.write("Found URL.")
    time.sleep(2)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=True)

st.button("Rerun")
