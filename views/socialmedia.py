import streamlit as st
from views.st_functions import st_button, load_css
from PIL import Image

load_css()
st.image("./assets/combined_logo.png", width=300)
st.title('FOLLOW US ON SOCIAL MEDIA!', anchor=False)
col1, col2 = st.columns(2)
#col2.image(Image.open('dp.png'))
with col1:



    icon_size = 20
    st_button('instagram', 'https://www.instagram.com/wasatchtrailscollective/', 'Instagram', icon_size)
    st_button('discord', 'https://discord.com/invite/UmG8HHa39A', 'Discord', icon_size)
    st_button('strava', 'https://www.strava.com/clubs/1136918', 'Strava', icon_size)
    st_button('','https://linktr.ee/wasatchtrailscollective', 'Linktree',icon_size)

with col2:

    st.image("./assets/follow_us.jpeg", width=390)