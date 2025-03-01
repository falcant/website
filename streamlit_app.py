import streamlit as st

#st.title("Hola que tal!")

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About WTC / Mission Statement",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/socialmedia.py",
    title="Social Media",
    icon=":material/favorite:",
)
project_2_page = st.Page(
    "views/calendar.py",
    title="Calendar",
    icon=":material/calendar_month:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Information": [about_page],
        "Resources": [project_1_page],
        "Events": [ project_2_page]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/combined_logo.png")
st.sidebar.markdown("Made with ❤️ by the [WTC](https://www.instagram.com/wasatchtrailscollective/)")


pg.run()
