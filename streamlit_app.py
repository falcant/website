import streamlit as st

#st.title("Hola que tal!")

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/resources.py",
    title="resources",
    icon=":material/brown_heart:",
)
project_2_page = st.Page(
    "views/events.py",
    title="Events",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

pg.run()
