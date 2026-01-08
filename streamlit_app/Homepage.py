#Homepage
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Internal Analytics Tool",
    layout="wide"
)

st.title("TDAS Productivity Tools App")
st.subheader("Created by Victor Bouret, Consultant at FTI within the TDAS team. This tool is designed to help you be more efficient in key routine tasks.")

st.markdown("""
## How to navigate:

Use the sidebar on the left to navigate to the specific analytics tools you would like to use.
            
## Tools:

There is a Jira tool and a Doc Review Excel sheet creator tool.
""")