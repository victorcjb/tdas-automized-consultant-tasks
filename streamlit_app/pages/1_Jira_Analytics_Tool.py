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
    st.text(f"Total rows in this dataset: {len(df)}")
    st.write("First 5 rows of your Jira export:")
    st.dataframe(df.head())
    if uploaded_file:
    #Data from 
        st.subheader("Column mapping")
        st.text("Please match the key columns below to the ones in your dataset.")
        columns = df.columns.tolist()
        ticket_number = st.selectbox("Select ticket id/number column", columns)
        created_date = st.selectbox("Select Created Date column", columns)
        closed_date = st.selectbox("Select Closed Date (Resolved Date if no closed) column", columns)
        priority_level = st.selectbox("Select Priority Level of Ticket Column", columns)
        status_level = st.selectbox("Select status column (closed, open, etc...)", columns)
        author_ticket = st.selectbox("Select author or created by column", columns)
        summary_col = st.selectbox("Select Summary column", columns)
        #Check to see uniqueness of columns
        selected_columns = [ticket_number, created_date, closed_date, priority_level, status_level, author_ticket, summary_col]
         # Check if any dropdown is not selected or duplicates exist
        if None in selected_columns or "" in selected_columns:
            st.error("⚠️ Please select all columns.")
        elif len(selected_columns) != len(set(selected_columns)):
            st.error("⚠️ Columns must be unique. Please select different columns for each field.")
        else:
            st.success("✅ Columns matched successfully!")

            missing_cols = [ticket_number, created_date, closed_date, priority_level, status_level, author_ticket, summary_col]
            missing = df[missing_cols].isna().sum()
            if uploaded_file:
                    # Calculate missing values in the selected columns
                    missing_cols = [ticket_number, created_date, closed_date, priority_level, status_level, author_ticket, summary_col]
                    missing = df[missing_cols].isna().sum()


                    

                # Show table only if missing values exist
            if missing.sum() > 0:
                    st.subheader("Missing values per selected column")
                    acknowledge = st.checkbox("I acknowledge the missing values below")
                    if acknowledge:
                        st.success("You have acknowledged the missing values.")
                    else:
                        st.text("For personal use: shows how many blank datapoints per column.")
                        st.text(f"Total rows in this dataset: {len(df)}")
                        st.write(missing)  # Show table if not acknowledged
            else:
                    st.success("✅ No missing values in the selected columns!")
