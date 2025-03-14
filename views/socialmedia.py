import streamlit as st
from views.st_functions import st_button, load_css
from PIL import Image

#load_css()
st.image("./assets/combined_logo.png", width=300)

st.write("""
    Stay connected and never miss a beat with the WTC! Join our online community to connect with fellow runners
        , share your progress, and be the first to know about special announcements.
     Don't just run with us, be part of our digital journey and stay up-to-date with all the latest happenings!
""")
st.title('FOLLOW US ON SOCIAL MEDIA!', anchor=False)
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
#col2.image(Image.open('dp.png'))
with col1:

    load_css()

    icon_size = 20
    st_button('instagram', 'https://www.instagram.com/wasatchtrailscollective/', 'Instagram', icon_size)
    st_button('discord', 'https://discord.com/invite/UmG8HHa39A', 'Discord', icon_size)
    st_button('strava', 'https://www.strava.com/clubs/1136918', 'Strava', icon_size)
    st_button('','https://linktr.ee/wasatchtrailscollective', 'Linktree',icon_size)

with col2:

    st.image("./assets/follow_us.png",output_format = "PNG")