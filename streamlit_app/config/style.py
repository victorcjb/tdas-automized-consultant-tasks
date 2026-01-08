#Styling defintion
import streamlit as st

STYLE = {
    "corporate_blue": "#003763",
    "medium_blue": "#0067B1",
    "light_teal_blue": "#00C9D4",
    "medium_gray": "#AFB2B3",
    "green":"#1BB680",
    "teal_blue":"#008FBE",
    "slate":"#5781A6",
    "tangerine":"#E1523D",
    "font": "Calibri"
}



def apply_global_styles():
    st.markdown(
        f"""
        <style>
        html, body, [class*="css"] {{
            color: {STYLE["corporate_blue"]} !important;
            font-family: {STYLE["font"]}, Calibri;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: {STYLE["medium_blue"]} !important;
            font-family: {STYLE["font"]}, Calibri;
        }}

        section[data-testid="stSidebar"] * {{
            color: {STYLE["medium_gray"]} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
