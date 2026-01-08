import streamlit as st
import pandas as pd
import plotly.express as px
from config.style import apply_global_styles
apply_global_styles()




# Initialize step
if "jira_step" not in st.session_state:
    st.session_state.jira_step = 1

# STEP 1: Upload + column mapping
if st.session_state.jira_step == 1:
    st.markdown("""
     ## Jira Analytics Tool""")
    st.write("This page contains all your Jira-related data and dashboards.")
    st.subheader("Setup Page")

    uploaded_file = st.file_uploader(
        "Upload Jira CSV or Excel report. Make sure created and closed date columns are in MM/DD/YYYY HH:MM format.",
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        # Read file
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state.df = df

        st.success("File loaded successfully!")
        st.text(f"Total rows in this dataset: {len(df)}")
        st.write("First 5 rows of your Jira export:")
        st.dataframe(df.head())

        # Column mapping
        st.subheader("Column mapping")
        st.text("Please match the key columns below to the ones in your dataset.")
        columns = df.columns.tolist()

        summary_col = st.selectbox("Select Summary column", columns, index=0)
        created_date = st.selectbox("Select Created Date column", columns, index=1)
        closed_date = st.selectbox("Select Closed Date (Resolved Date if no closed) column", columns, index=2)
        priority_level = st.selectbox("Select Priority Level of Ticket Column", columns, index=3)
        status_level = st.selectbox("Select status column (closed, open, etc...)", columns, index=4)
        author_ticket = st.selectbox("Select author or created by column", columns, index=5)
        ticket_number = st.selectbox("Select ticket id/number column", columns, index=6)

        # Save selected columns to session_state
        st.session_state.selected_columns = {
            "summary_col": summary_col,
            "created_date": created_date,
            "closed_date": closed_date,
            "priority_level": priority_level,
            "status_level": status_level,
            "author_ticket": author_ticket,
            "ticket_number": ticket_number
        }

        # Check uniqueness
        if len(set(st.session_state.selected_columns.values())) != 7:
            st.error("⚠️ Columns must be unique.")
        else:
            st.success("✅ Columns matched successfully!")

            # Missing values
            missing = df[list(st.session_state.selected_columns.values())].isna().sum()
            if missing.sum() > 0:
                st.subheader("Missing values per selected column")
                acknowledge = st.checkbox("I acknowledge the missing values below")
                if not acknowledge:
                    st.text("For personal use: shows how many blank datapoints per column.")
                    st.text(f"Total rows in this dataset: {len(df)}")
                    st.write(missing)
                else:
                    st.success("You have acknowledged the missing values.")

            # Continue button
            ready_to_analyze = (missing.sum() == 0) or acknowledge
            if ready_to_analyze:
                if st.button("Continue to Analysis ➡️"):
                    st.session_state.jira_step = 2


# STEP 2: Analytics Dashboard
elif st.session_state.jira_step == 2:
    # Load df and selected columns from session state
    df = st.session_state.df
    sel = st.session_state.selected_columns

    st.subheader("Data Dashboard")
    st.text(f"Total rows: {len(df)}")
    st.dataframe(df.head())

    # Convert dates strictly
    df[sel["created_date"]] = pd.to_datetime(df[sel["created_date"]], format="%m/%d/%Y %H:%M", errors="raise")
    df[sel["closed_date"]] = pd.to_datetime(df[sel["closed_date"]], format="%m/%d/%Y %H:%M", errors="raise")

    # Compute duration
    df['duration_days'] = (df[sel["closed_date"]] - df[sel["created_date"]]).dt.days

    # Priority pie chart
    priority_counts = df[sel["priority_level"]].value_counts().reset_index()
    priority_counts.columns = ['priority', 'count']

    fig_priority = px.pie(
        priority_counts,
        names='priority',
        values='count',
        title='Ticket Priority Breakdown',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_priority, use_container_width=True)

    # Duration histogram
    fig_duration = px.histogram(
        df,
        x='duration_days',
        nbins=20,
        title='Ticket Duration (Days)',
        color=df[sel["priority_level"]],
        barmode='overlay',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_duration, use_container_width=True)
