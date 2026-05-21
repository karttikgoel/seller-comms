import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Email Builder", page_icon="✉️")

with open("assets/email_builder.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=900, scrolling=True)
