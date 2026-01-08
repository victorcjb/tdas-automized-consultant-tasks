#Application initial
import streamlit as st
import pandas as pd

#Build Sidebar tool and page headers for Jira/Doc Review tool
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
    uploaded_file = st.file_uploader(
        "Upload Jira CSV or Excel report",
        type=["csv","xslx"]
    )
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_xlsx(uploaded_file)
        st.success("File loaded successfully!")
        st.write("First 5 rows of your Jira export:")
        st.dataframe(df.head())
        
elif page == "Document Review":
    st.header("Document Review Builder")
    st.write("Select a folder to generate a doc review log.")

