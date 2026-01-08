#Jira tab
import streamlit as st
import pandas as pd

#Build Sidebar tool and page headers for Jira/Doc Review tool
st.set_page_config(page_title="Jira Analytics")

st.title("Jira Analytics Tool")
st.write("This page contains all your Jira-related dashboards and data.")


st.header("Jira Analytics")
#only supports csv and xlsx files. No other formats.
uploaded_file = st.file_uploader(
    "Upload Jira CSV or Excel report",
    type=["csv","xslx"]
)
#Determine if file uploaded was csv or xlsx
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_xlsx(uploaded_file)
    #File Preview Code
    st.success("File loaded successfully!")
    st.write("First 5 rows of your Jira export:")
    st.dataframe(df.head())
    if uploaded_file:
    #Data from 
        st.subheader("Column mapping")
        st.text("Please match the key columns below to the ones your dataset.")
        columns = df.columns.tolist()
        ticket_number = st.selectbox("Select ticket id/number column", columns)
        created_date = st.selectbox("Select Created Date column", columns)
        closed_date = st.selectbox("Select Closed Date (Resolved Date if no closed) column", columns)
        priority_level = st.selectbox("Select Priority Level of Ticket Column", columns)
        status_level = st.selectbox("Select status column (closed, open, etc...)", columns)
        author_ticket = st.selectbox("Select author or created by column", columns)
        summary_col = st.selectbox("Select Summary column", columns)
        
