#Application initial

import streamlit as st

st.set_page_config(
    page_title="Internal Analytics Tool",
    layout="wide"
)

st.title("Internal Analytics Tool")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Jira Analytics", "Document Review"]
)

if page == "Jira Analytics":
    st.header("Jira Analytics")
    st.write("Upload a Jira export to begin.")

elif page == "Document Review":
    st.header("Document Review Builder")
    st.write("Select a folder to generate a doc review log.")
