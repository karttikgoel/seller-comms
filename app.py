import streamlit as st

home_page = st.Page("pages/home.py", title="Home", url_path="/", icon="📬", default=True)
email_map_page = st.Page("pages/email_map.py", title="Email Map", url_path="email-map", icon="🗺️")
email_builder_page = st.Page("pages/email_builder.py", title="Email Builder", url_path="email-builder", icon="✉️")

pg = st.navigation([home_page, email_map_page, email_builder_page], position="hidden")
pg.run()
