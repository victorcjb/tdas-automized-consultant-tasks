#Jira tab
import streamlit as st
import pandas as pd
from config.style import apply_global_styles
apply_global_styles()

#Build Sidebar tool and page headers for Jira/Doc Review tool
st.markdown("""
     ## Document Review Excel Creation Tab""")

st.title("Document Review Excel Creation Tab")
st.write("This page contains tool to select folder and create live excel document sheet.")