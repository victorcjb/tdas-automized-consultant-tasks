#Homepage
from pathlib import Path
import streamlit as st
import pandas as pd
from config.style import apply_global_styles
apply_global_styles()

#LOGO Path
BASE_DIR = Path(__file__).resolve().parent.parent
logo_path = BASE_DIR / "assets" / "FTI_LOGO_Blue-JPG.jpg"



st.set_page_config(
    page_title="Internal Analytics Tool",
    layout="wide"
)

st.image(str(logo_path), width=200)

st.markdown("""
 ## TDAS Productivity Tools App""")

st.markdown("""
#### How to navigate:

Use the sidebar on the left to navigate to the specific analytics tools you would like to use.
            
#### Tools:

There is a Jira tool and a Doc Review Excel sheet creator tool.
            

""")
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.text("")  # one line space
st.text("")  # another line space
st.markdown("""
#### Created by Victor Bouret, Consultant at FTI within the TDAS team. This tool is designed to help you be more efficient in key routine tasks.
           """)
